def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, -4, -6], [-6, -5, -8], [3, 3, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, -4, -6], [-6, -5, -8], [3, 3, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, 6, 7, -6, 5, 3], [4, -8, -5, 5, -9, 3], [-3, 1, -2, 6, -6, 2], [-8, -6, -3, -8, -9, -5], [-5, -8, -8, -1, 5, -9]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, 6, 7, -6, 5, 3], [4, -8, -5, 5, -9, 3], [-3, 1, -2, 6, -6, 2], [-8, -6, -3, -8, -9, -5], [-5, -8, -8, -1, 5, -9]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -1], [-1, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -1], [-1, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[100, 50, -50], [10, -10, -10], [10, 10, -10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[100, 50, -50], [10, -10, -10], [10, 10, -10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -6, -3], [-2, -3, -3, -5], [-1, -3, -5, -7], [-8, -8, -3, -4]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -6, -3], [-2, -3, -3, -5], [-1, -3, -5, -7], [-8, -8, -3, -4]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -1, 1], [-1, -2, -2], [-3, 3, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -1, 1], [-1, -2, -2], [-3, 3, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-3, 5, -10], [0, 0, -3], [3, 1, -2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-3, 5, -10], [0, 0, -3], [3, 1, -2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -50, 20], [-30, -10, 10], [10, 30, -5]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -50, 20], [-30, -10, 10], [10, 30, -5]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -1, -1], [-1, -1, -1], [-1, -1, 100]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -1, -1], [-1, -1, -1], [-1, -1, 100]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -1, 1, -1, 1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -1, 1, -1, 1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 3, -5], [-5, -10, 1, 20], [10, 30, -5, 15], [-10, -20, 5, 30]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 3, -5], [-5, -10, 1, 20], [10, 30, -5, 15], [-10, -20, 5, 30]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -15, 20, -25, 30], [-35, 40, -45, 50, -55], [60, -65, 70, -75, 80], [-85, 90, -95, 100, -105], [110, -115, 120, -125, 130]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -15, 20, -25, 30], [-35, 40, -45, 50, -55], [60, -65, 70, -75, 80], [-85, 90, -95, 100, -105], [110, -115, 120, -125, 130]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30, 40], [-50, -60, 70, -80], [90, -100, 110, -120], [-130, 140, -150, 160]]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30, 40], [-50, -60, 70, -80], [90, -100, 110, -120], [-130, 140, -150, 160]]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, 20, -30, 40, -50, 60], [-20, 30, -40, 50, -60, 70], [30, -40, 50, -60, 70, -80], [40, -50, 60, -70, 80, -90]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, 20, -30, 40, -50, 60], [-20, 30, -40, 50, -60, 70], [30, -40, 50, -60, 70, -80], [40, -50, 60, -70, 80, -90]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, -10, 20, -30, 40], [10, -20, 30, -40, 50], [-10, 20, -30, 40, -50], [20, -30, 40, -50, 60], [-30, 40, -50, 60, -70]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, -10, 20, -30, 40], [10, -20, 30, -40, 50], [-10, 20, -30, 40, -50], [20, -30, 40, -50, 60], [-30, 40, -50, 60, -70]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5], [-4, -5, -6], [-5, -6, -7]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5], [-4, -5, -6], [-5, -6, -7]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15], [-4, -8, -12, -16, -20], [-5, -10, -15, -20, -25]]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15], [-4, -8, -12, -16, -20], [-5, -10, -15, -20, -25]]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -20, -20, -20], [20, 20, 20, 20], [-10, -10, -10, -10], [10, 10, 10, 10]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -20, -20, -20], [20, 20, 20, 20], [-10, -10, -10, -10], [10, 10, 10, 10]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, 0, 5, -10, 10], [-2, 3, -4, 5, -6], [0, 1, -2, 3, -4], [5, -6, 7, -8, 9], [10, -11, 12, -13, 14]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, 0, 5, -10, 10], [-2, 3, -4, 5, -6], [0, 1, -2, 3, -4], [5, -6, 7, -8, 9], [10, -11, 12, -13, 14]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-100, -200, 300], [400, -500, 100], [-200, 100, -300], [50, 100, -100]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-100, -200, 300], [400, -500, 100], [-200, 100, -300], [50, 100, -100]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, -30]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, -30]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-30, -20, -10], [0, 10, 20], [10, 20, 30], [-10, -20, -30]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-30, -20, -10], [0, 10, 20], [10, 20, 30], [-10, -20, -30]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, -5, -5, -5], [-5, 0, 0, -5], [-5, 0, 0, -5], [-5, -5, -5, -5]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, -5, -5, -5], [-5, 0, 0, -5], [-5, 0, 0, -5], [-5, -5, -5, -5]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1000, -1000, 1000, -1000], [1000, 1000, -1000, 1000], [-1000, 1000, 1000, -1000], [-1000, -1000, 1000, 1000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1000, -1000, 1000, -1000], [1000, 1000, -1000, 1000], [-1000, 1000, 1000, -1000], [-1000, -1000, 1000, 1000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000]]) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000]]) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-500, 500, -500, 500], [500, -500, 500, -500], [-500, 500, -500, 500], [500, -500, 500, -1]]) == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-500, 500, -500, 500], [500, -500, 500, -500], [-500, 500, -500, 500], [500, -500, 500, -1]]) == 501: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-50, -10, -20, -15], [20, 30, -10, 10], [-5, 15, 20, -20], [10, -10, 30, -30]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-50, -10, -20, -15], [20, 30, -10, 10], [-5, 15, 20, -20], [10, -10, 30, -30]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 40, 10], [-15, -25, 35, 5], [-10, -5, 25, -5], [5, 10, -15, 20]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 40, 10], [-15, -25, 35, 5], [-10, -5, 25, -5], [5, 10, -15, 20]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 10, 50], [-50, -10, 20, 30], [-10, 5, -100, 10], [100, 10, -5, 20]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 10, 50], [-50, -10, 20, 30], [-10, 5, -100, 10], [100, 10, -5, 20]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -10, 20, -20, 30], [-30, 40, -50, 60, -70], [80, -90, 100, -110, 120], [-130, 140, -150, 160, -170]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -10, 20, -20, 30], [-30, 40, -50, 60, -70], [80, -90, 100, -110, 120], [-130, 140, -150, 160, -170]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[100, -100, 200, -200], [-200, 300, -300, 400], [400, -400, 500, -500], [-500, 600, -600, 700]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[100, -100, 200, -200], [-200, 300, -300, 400], [400, -400, 500, -500], [-500, 600, -600, 700]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4, -5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4, -5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30, -40, -50], [-9, -18, -27, -36, -45], [-8, -16, -24, -32, -40], [-7, -14, -21, -28, -35], [-6, -12, -18, -24, -30]]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30, -40, -50], [-9, -18, -27, -36, -45], [-8, -16, -24, -32, -40], [-7, -14, -21, -28, -35], [-6, -12, -18, -24, -30]]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4, -5, 6, 7, 8, 9, 10], [-10, -9, -8, -7, -6, 5, 4, 3, 2, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4, -5, 6, 7, 8, 9, 10], [-10, -9, -8, -7, -6, 5, 4, 3, 2, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 40, 50], [-10, -20, -10, 10], [30, 10, -20, -30], [50, 50, 50, -5]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 40, 50], [-10, -20, -10, 10], [30, 10, -20, -30], [50, 50, 50, -5]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 30, -50], [10, 20, -40, 60], [-30, -40, 20, -10], [50, 10, -20, -60]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 30, -50], [10, 20, -40, 60], [-30, -40, 20, -10], [50, 10, -20, -60]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -3, 2, 4, -1], [2, -2, 3, -2, -2], [1, -1, -2, -3, 3], [-1, 3, -2, -3, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -3, 2, 4, -1], [2, -2, 3, -2, -2], [1, -1, -2, -3, 3], [-1, 3, -2, -3, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, -10, 5, 0, 0], [-5, 0, 0, -10, -1], [0, 0, 10, 0, -20], [0, 10, -20, 0, 10], [-10, -20, 0, 10, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, -10, 5, 0, 0], [-5, 0, 0, -10, -1], [0, 0, 10, 0, -20], [0, 10, -20, 0, 10], [-10, -20, 0, 10, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -1, -6], [-1, 10, -1], [-2, -3, -4], [1, 2, -5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -1, -6], [-1, 10, -1], [-2, -3, -4], [1, 2, -5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -10, 20, -20], [5, -5, 10, -10], [0, 0, 0, 0], [-5, 5, -15, 15]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -10, 20, -20], [5, -5, 10, -10], [0, 0, 0, 0], [-5, 5, -15, 15]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -4], [2, 1, 0, -1, -2, -3, -4, -5, -4, -3], [1, 0, -1, -2, -3, -4, -5, -4, -3, -2], [0, -1, -2, -3, -4, -5, -4, -3, -2, -1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -4], [2, 1, 0, -1, -2, -3, -4, -5, -4, -3], [1, 0, -1, -2, -3, -4, -5, -4, -3, -2], [0, -1, -2, -3, -4, -5, -4, -3, -2, -1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4, -5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-5, -4, -3, -2, -1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4, -5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-5, -4, -3, -2, -1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30, -40], [-30, -40, -50, -60], [-40, -50, -60, -70], [-50, -60, -70, -80]]) == 311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30, -40], [-30, -40, -50, -60], [-40, -50, -60, -70], [-50, -60, -70, -80]]) == 311: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, -2, -5], [-3, -2, -2, -5], [-2, -2, -2, -5], [-5, -5, -5, -20]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, -2, -5], [-3, -2, -2, -5], [-2, -2, -2, -5], [-5, -5, -5, -20]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, 100]]) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, 100]]) == 301: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 100, 200, -300], [100, -200, -300, 400], [200, -300, 400, -500], [300, 400, -500, 600]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 100, 200, -300], [100, -200, -300, 400], [200, -300, 400, -500], [300, 400, -500, 600]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -15, -10, -5], [-10, -5, 0, 5], [0, 5, 10, 15], [5, 10, 15, 20]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -15, -10, -5], [-10, -5, 0, 5], [0, 5, 10, 15], [5, 10, 15, 20]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -15, 10], [-10, 20, -10], [10, -5, 20], [-15, 10, -20]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -15, 10], [-10, 20, -10], [10, -5, 20], [-15, 10, -20]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, 10, 15, -20], [-10, 20, -15, 25], [5, -10, 30, -35], [-15, 25, -20, 30]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, 10, 15, -20], [-10, 20, -15, 25], [5, -10, 30, -35], [-15, 25, -20, 30]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-100, -200, 300], [-400, -500, 600], [700, 800, -900]]) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-100, -200, 300], [-400, -500, 600], [700, 800, -900]]) == 301: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30, -40], [-40, -50, -60, -70], [-70, -80, -90, -100], [100, 100, 100, 100]]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30, -40], [-40, -50, -60, -70], [-70, -80, -90, -100], [100, 100, 100, 100]]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 1000]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 1000]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, -10, 15, -20, 25], [-30, 35, -40, 45, -50], [-60, 65, -70, 75, -80], [-90, 95, -100, 105, -110], [120, -125, 130, -135, 140]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, -10, 15, -20, 25], [-30, 35, -40, 45, -50], [-60, 65, -70, 75, -80], [-90, 95, -100, 105, -110], [120, -125, 130, -135, 140]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 30, -10], [10, -5, -50, 20], [0, 20, -30, 10], [-10, 50, -10, 20]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 30, -10], [10, -5, -50, 20], [0, 20, -30, 10], [-10, 50, -10, 20]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-100, 100, -50, 50], [-200, 200, -150, 150], [100, -100, 50, -50], [-50, 50, -25, 25]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-100, 100, -50, 50], [-200, 200, -150, 150], [100, -100, 50, -50], [-50, 50, -25, 25]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[100, -100, 0, -100], [100, -100, 0, 100], [0, 100, -100, 0], [-100, 0, 100, -100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[100, -100, 0, -100], [100, -100, 0, 100], [0, 100, -100, 0], [-100, 0, 100, -100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -30, 20, -40, 50], [30, -10, -50, 10, 0], [0, 20, 30, -20, -10], [-10, 10, 20, -30, 40], [-50, 40, -30, 20, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -30, 20, -40, 50], [30, -10, -50, 10, 0], [0, 20, 30, -20, -10], [-10, 10, 20, -30, 40], [-50, 40, -30, 20, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 4, 1], [-3, -2, 1, -1], [3, -4, 2, -4], [4, 2, -4, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 4, 1], [-3, -2, 1, -1], [3, -4, 2, -4], [4, 2, -4, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 3, -4], [3, -5, -10, 1], [10, 30, -5, 20], [10, 10, -10, -20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 3, -4], [3, -5, -10, 1], [10, 30, -5, 20], [10, 10, -10, -20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[0, -5, 10, -10, 20], [-5, 10, -5, 0, 5], [10, -5, 0, 5, -10], [0, 5, -10, 15, -5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[0, -5, 10, -10, 20], [-5, 10, -5, 0, 5], [10, -5, 0, 5, -10], [0, 5, -10, 15, -5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, 10, -30, 40], [-10, -5, 5, -15], [20, -20, 10, -10], [-30, 20, -10, 5]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, 10, -30, 40], [-10, -5, 5, -15], [20, -20, 10, -10], [-30, 20, -10, 5]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4, -5], [-5, -6, -7, -8, -9], [-9, -10, -11, -12, -13], [-13, -14, -15, -16, -17], [-17, -18, -19, -20, 100]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4, -5], [-5, -6, -7, -8, -9], [-9, -10, -11, -12, -13], [-13, -14, -15, -16, -17], [-17, -18, -19, -20, 100]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -1, -10], [-5, -5, -5], [-2, -1, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -1, -10], [-5, -5, -5], [-2, -1, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-5, -10, 100], [-50, -100, 200], [-100, -200, 300], [-200, -300, 400]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-5, -10, 100], [-50, -100, 200], [-100, -200, 300], [-200, -300, 400]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -3, -5, -7], [-9, -11, -13, -15], [-17, -19, -21, -23], [-25, -27, -29, -31]]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -3, -5, -7], [-9, -11, -13, -15], [-17, -19, -21, -23], [-25, -27, -29, -31]]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, 100]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, 100]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 3, -5], [1, 2, -4, 6], [-3, -4, 2, -1], [5, 1, -2, -6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 3, -5], [1, 2, -4, 6], [-3, -4, 2, -1], [5, 1, -2, -6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[10, -10, 0, 10], [-10, 10, -10, 10], [0, -10, 10, -10], [10, -10, 10, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[10, -10, 0, 10], [-10, 10, -10, 10], [0, -10, 10, -10], [10, -10, 10, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-20, -30, 10, 50], [-10, -40, 20, 10], [30, -10, -20, 40], [-50, 10, 5, -15]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-20, -30, 10, 50], [-10, -40, 20, 10], [30, -10, -20, 40], [-50, 10, 5, -15]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-2, -3, 3, -4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-2, -3, 3, -4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[1, -1, -1, 1], [-1, -2, -1, 1], [-1, -2, -1, -1], [1, 1, -1, -1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[1, -1, -1, 1], [-1, -2, -1, 1], [-1, -2, -1, -1], [1, 1, -1, -1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]) == 3
    assert candidate(dungeon = [[-5, -4, -6], [-6, -5, -8], [3, 3, 1]]) == 12
    assert candidate(dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
    assert candidate(dungeon = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 1
    assert candidate(dungeon = [[1, 6, 7, -6, 5, 3], [4, -8, -5, 5, -9, 3], [-3, 1, -2, 6, -6, 2], [-8, -6, -3, -8, -9, -5], [-5, -8, -8, -1, 5, -9]]) == 1
    assert candidate(dungeon = [[-2, -1], [-1, 10]]) == 4
    assert candidate(dungeon = [[0]]) == 1
    assert candidate(dungeon = [[100, 50, -50], [10, -10, -10], [10, 10, -10]]) == 1
    assert candidate(dungeon = [[-1, -2, -6, -3], [-2, -3, -3, -5], [-1, -3, -5, -7], [-8, -8, -3, -4]]) == 20
    assert candidate(dungeon = [[-2, -1, 1], [-1, -2, -2], [-3, 3, 1]]) == 5
    assert candidate(dungeon = [[-3, 5, -10], [0, 0, -3], [3, 1, -2]]) == 4
    assert candidate(dungeon = [[-10, -50, 20], [-30, -10, 10], [10, 30, -5]]) == 41
    assert candidate(dungeon = [[-1, -1, -1], [-1, -1, -1], [-1, -1, 100]]) == 5
    assert candidate(dungeon = [[1, -1, 1, -1, 1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 1
    assert candidate(dungeon = [[-2, -3, 3, -5], [-5, -10, 1, 20], [10, 30, -5, 15], [-10, -20, 5, 30]]) == 6
    assert candidate(dungeon = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 1
    assert candidate(dungeon = [[10, -15, 20, -25, 30], [-35, 40, -45, 50, -55], [60, -65, 70, -75, 80], [-85, 90, -95, 100, -105], [110, -115, 120, -125, 130]]) == 21
    assert candidate(dungeon = [[-10, -20, -30, 40], [-50, -60, 70, -80], [90, -100, 110, -120], [-130, 140, -150, 160]]) == 61
    assert candidate(dungeon = [[-10, 20, -30, 40, -50, 60], [-20, 30, -40, 50, -60, 70], [30, -40, 50, -60, 70, -80], [40, -50, 60, -70, 80, -90]]) == 11
    assert candidate(dungeon = [[0, -10, 20, -30, 40], [10, -20, 30, -40, 50], [-10, 20, -30, 40, -50], [20, -30, 40, -50, 60], [-30, 40, -50, 60, -70]]) == 11
    assert candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1
    assert candidate(dungeon = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1
    assert candidate(dungeon = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5], [-4, -5, -6], [-5, -6, -7]]) == 29
    assert candidate(dungeon = [[-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15], [-4, -8, -12, -16, -20], [-5, -10, -15, -20, -25]]) == 86
    assert candidate(dungeon = [[-20, -20, -20, -20], [20, 20, 20, 20], [-10, -10, -10, -10], [10, 10, 10, 10]]) == 21
    assert candidate(dungeon = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]]) == 2
    assert candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 1
    assert candidate(dungeon = [[-5, 0, 5, -10, 10], [-2, 3, -4, 5, -6], [0, 1, -2, 3, -4], [5, -6, 7, -8, 9], [10, -11, 12, -13, 14]]) == 6
    assert candidate(dungeon = [[-100, -200, 300], [400, -500, 100], [-200, 100, -300], [50, 100, -100]]) == 101
    assert candidate(dungeon = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 2
    assert candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, -30]]) == 11
    assert candidate(dungeon = [[-30, -20, -10], [0, 10, 20], [10, 20, 30], [-10, -20, -30]]) == 31
    assert candidate(dungeon = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 2
    assert candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1
    assert candidate(dungeon = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 10
    assert candidate(dungeon = [[-5, -5, -5, -5], [-5, 0, 0, -5], [-5, 0, 0, -5], [-5, -5, -5, -5]]) == 21
    assert candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 1
    assert candidate(dungeon = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 1
    assert candidate(dungeon = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 1
    assert candidate(dungeon = [[100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100], [100, -100, 100, -100]]) == 1
    assert candidate(dungeon = [[1000, -1000, 1000, -1000], [1000, 1000, -1000, 1000], [-1000, 1000, 1000, -1000], [-1000, -1000, 1000, 1000]]) == 1
    assert candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000]]) == 1001
    assert candidate(dungeon = [[-500, 500, -500, 500], [500, -500, 500, -500], [-500, 500, -500, 500], [500, -500, 500, -1]]) == 501
    assert candidate(dungeon = [[-50, -10, -20, -15], [20, 30, -10, 10], [-5, 15, 20, -20], [10, -10, 30, -30]]) == 51
    assert candidate(dungeon = [[-20, -30, 40, 10], [-15, -25, 35, 5], [-10, -5, 25, -5], [5, 10, -15, 20]]) == 46
    assert candidate(dungeon = [[-20, -30, 10, 50], [-50, -10, 20, 30], [-10, 5, -100, 10], [100, 10, -5, 20]]) == 51
    assert candidate(dungeon = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 2
    assert candidate(dungeon = [[10, -10, 20, -20, 30], [-30, 40, -50, 60, -70], [80, -90, 100, -110, 120], [-130, 140, -150, 160, -170]]) == 31
    assert candidate(dungeon = [[100, -100, 200, -200], [-200, 300, -300, 400], [400, -400, 500, -500], [-500, 600, -600, 700]]) == 1
    assert candidate(dungeon = [[-1, -2, -3, -4, -5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 2
    assert candidate(dungeon = [[-10, -20, -30, -40, -50], [-9, -18, -27, -36, -45], [-8, -16, -24, -32, -40], [-7, -14, -21, -28, -35], [-6, -12, -18, -24, -30]]) == 125
    assert candidate(dungeon = [[-1, -2, -3, -4, -5, 6, 7, 8, 9, 10], [-10, -9, -8, -7, -6, 5, 4, 3, 2, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 12
    assert candidate(dungeon = [[-20, -30, 40, 50], [-10, -20, -10, 10], [30, 10, -20, -30], [50, 50, 50, -5]]) == 31
    assert candidate(dungeon = [[-20, -30, 30, -50], [10, 20, -40, 60], [-30, -40, 20, -10], [50, 10, -20, -60]]) == 41
    assert candidate(dungeon = [[1, -3, 2, 4, -1], [2, -2, 3, -2, -2], [1, -1, -2, -3, 3], [-1, 3, -2, -3, 4]]) == 1
    assert candidate(dungeon = [[0, -10, 5, 0, 0], [-5, 0, 0, -10, -1], [0, 0, 10, 0, -20], [0, 10, -20, 0, 10], [-10, -20, 0, 10, 0]]) == 6
    assert candidate(dungeon = [[-2, -1, -6], [-1, 10, -1], [-2, -3, -4], [1, 2, -5]]) == 4
    assert candidate(dungeon = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]]) == 1
    assert candidate(dungeon = [[10, -10, 20, -20], [5, -5, 10, -10], [0, 0, 0, 0], [-5, 5, -15, 15]]) == 1
    assert candidate(dungeon = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -4], [2, 1, 0, -1, -2, -3, -4, -5, -4, -3], [1, 0, -1, -2, -3, -4, -5, -4, -3, -2], [0, -1, -2, -3, -4, -5, -4, -3, -2, -1]]) == 12
    assert candidate(dungeon = [[-1, -2, -3, -4, -5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-5, -4, -3, -2, -1]]) == 2
    assert candidate(dungeon = [[-10, -20, -30, -40], [-30, -40, -50, -60], [-40, -50, -60, -70], [-50, -60, -70, -80]]) == 311
    assert candidate(dungeon = [[-2, -3, -2, -5], [-3, -2, -2, -5], [-2, -2, -2, -5], [-5, -5, -5, -20]]) == 37
    assert candidate(dungeon = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 1
    assert candidate(dungeon = [[-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, -50], [-50, -50, -50, 100]]) == 301
    assert candidate(dungeon = [[-1, 100, 200, -300], [100, -200, -300, 400], [200, -300, 400, -500], [300, 400, -500, 600]]) == 2
    assert candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29
    assert candidate(dungeon = [[-20, -15, -10, -5], [-10, -5, 0, 5], [0, 5, 10, 15], [5, 10, 15, 20]]) == 31
    assert candidate(dungeon = [[10, -15, 10], [-10, 20, -10], [10, -5, 20], [-15, 10, -20]]) == 1
    assert candidate(dungeon = [[-5, 10, 15, -20], [-10, 20, -15, 25], [5, -10, 30, -35], [-15, 25, -20, 30]]) == 6
    assert candidate(dungeon = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 1
    assert candidate(dungeon = [[-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 1001
    assert candidate(dungeon = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 6
    assert candidate(dungeon = [[-100, -200, 300], [-400, -500, 600], [700, 800, -900]]) == 301
    assert candidate(dungeon = [[-10, -20, -30, -40], [-40, -50, -60, -70], [-70, -80, -90, -100], [100, 100, 100, 100]]) == 121
    assert candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 1000]]) == 7
    assert candidate(dungeon = [[-5, -10, 15, -20, 25], [-30, 35, -40, 45, -50], [-60, 65, -70, 75, -80], [-90, 95, -100, 105, -110], [120, -125, 130, -135, 140]]) == 16
    assert candidate(dungeon = [[-20, -30, 30, -10], [10, -5, -50, 20], [0, 20, -30, 10], [-10, 50, -10, 20]]) == 21
    assert candidate(dungeon = [[-100, 100, -50, 50], [-200, 200, -150, 150], [100, -100, 50, -50], [-50, 50, -25, 25]]) == 101
    assert candidate(dungeon = [[100, -100, 0, -100], [100, -100, 0, 100], [0, 100, -100, 0], [-100, 0, 100, -100]]) == 1
    assert candidate(dungeon = [[10, -30, 20, -40, 50], [30, -10, -50, 10, 0], [0, 20, 30, -20, -10], [-10, 10, 20, -30, 40], [-50, 40, -30, 20, 10]]) == 1
    assert candidate(dungeon = [[-2, -3, 4, 1], [-3, -2, 1, -1], [3, -4, 2, -4], [4, 2, -4, 3]]) == 6
    assert candidate(dungeon = [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2
    assert candidate(dungeon = [[-2, -3, 3, -4], [3, -5, -10, 1], [10, 30, -5, 20], [10, 10, -10, -20]]) == 3
    assert candidate(dungeon = [[0, -5, 10, -10, 20], [-5, 10, -5, 0, 5], [10, -5, 0, 5, -10], [0, 5, -10, 15, -5]]) == 6
    assert candidate(dungeon = [[-20, 10, -30, 40], [-10, -5, 5, -15], [20, -20, 10, -10], [-30, 20, -10, 5]]) == 21
    assert candidate(dungeon = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 10]]) == 7
    assert candidate(dungeon = [[-1, -2, -3, -4, -5], [-5, -6, -7, -8, -9], [-9, -10, -11, -12, -13], [-13, -14, -15, -16, -17], [-17, -18, -19, -20, 100]]) == 55
    assert candidate(dungeon = [[-1, -1, -10], [-5, -5, -5], [-2, -1, 10]]) == 9
    assert candidate(dungeon = [[-5, -10, 100], [-50, -100, 200], [-100, -200, 300], [-200, -300, 400]]) == 16
    assert candidate(dungeon = [[-1, -3, -5, -7], [-9, -11, -13, -15], [-17, -19, -21, -23], [-25, -27, -29, -31]]) == 86
    assert candidate(dungeon = [[-10, -20, -30], [10, 20, 30], [-10, -20, -30], [10, 20, 30], [-10, -20, 100]]) == 11
    assert candidate(dungeon = [[-2, -3, 3, -5], [1, 2, -4, 6], [-3, -4, 2, -1], [5, 1, -2, -6]]) == 5
    assert candidate(dungeon = [[10, -10, 0, 10], [-10, 10, -10, 10], [0, -10, 10, -10], [10, -10, 10, 0]]) == 1
    assert candidate(dungeon = [[-20, -30, 10, 50], [-10, -40, 20, 10], [30, -10, -20, 40], [-50, 10, 5, -15]]) == 31
    assert candidate(dungeon = [[-2, -3, 3, -4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 6
    assert candidate(dungeon = [[1, -1, -1, 1], [-1, -2, -1, 1], [-1, -2, -1, -1], [1, 1, -1, -1]]) == 2
    assert candidate(dungeon = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == 29


