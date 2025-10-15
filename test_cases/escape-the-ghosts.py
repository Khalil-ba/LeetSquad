def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4]],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4]],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 3]],target = [0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 3]],target = [0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2]],target = [-3, -3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2]],target = [-3, -3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10000, -10000]],target = [-9999, -9999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10000, -10000]],target = [-9999, -9999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 100]],target = [-100, -100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 100]],target = [-100, -100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10000, 10000]],target = [-10000, -10000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10000, 10000]],target = [-10000, -10000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10000, 10000], [-10000, -10000]],target = [5000, 5000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10000, 10000], [-10000, -10000]],target = [5000, 5000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0]],target = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0]],target = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 100], [99, 100], [100, 99]],target = [101, 101]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 100], [99, 100], [100, 99]],target = [101, 101]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [5, 6], [6, 5], [6, 6]],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [5, 6], [6, 5], [6, 6]],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[2, 0]],target = [1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[2, 0]],target = [1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2]],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2]],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1]],target = [-2, -2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1]],target = [-2, -2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, 1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, 1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10000, 10000]],target = [9999, 9999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10000, 10000]],target = [9999, 9999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [2, 2]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [2, 2]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-2, -2], [-3, -3]],target = [-4, -4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-2, -2], [-3, -3]],target = [-4, -4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 0], [0, -1]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 0], [0, -1]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0]],target = [2, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0]],target = [2, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 1], [1, 1]],target = [-1, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 1], [1, 1]],target = [-1, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-5, 5], [5, -5], [0, 10]],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-5, 5], [5, -5], [0, 10]],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [3, 3], [-1, -1]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [3, 3], [-1, -1]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [1001, 1001]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [1001, 1001]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -2], [-2, -3], [-3, -4], [-4, -5], [-5, -6], [-6, -7]],target = [-7, -8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -2], [-2, -3], [-3, -4], [-4, -5], [-5, -6], [-6, -7]],target = [-7, -8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 1]],target = [-1, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 1]],target = [-1, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0], [0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-100, 100], [100, -100], [50, 50]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-100, 100], [100, -100], [50, 50]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10, 10], [10, -10], [-10, 10], [-10, -10]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10, 10], [10, -10], [-10, 10], [-10, -10]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],target = [2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],target = [2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [1, 1]],target = [10000, 10000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [1, 1]],target = [10000, 10000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10000, 0], [0, 10000], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10000, 0], [0, 10000], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-1, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-1, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [-1, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [-1, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],target = [9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],target = [9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],target = [6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],target = [6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [-2, 0], [0, -2], [2, 0], [0, 2]],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [-2, 0], [0, -2], [2, 0], [0, 2]],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-1, 1], [1, -1], [1, 1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-1, 1], [1, -1], [1, 1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, 10], [10, -10], [-10, -10]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, 10], [10, -10], [-10, -10]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, 0], [0, -10], [10, 0], [0, 10]],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, 0], [0, -10], [10, 0], [0, 10]],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10000, -10000], [-10000, 10000], [10000, -10000], [10000, 10000]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10000, -10000], [-10000, 10000], [10000, -10000], [10000, 10000]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, -5], [-5, 5], [0, 0]],target = [-3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, -5], [-5, 5], [0, 0]],target = [-3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [2, 1], [3, 3], [4, 4], [5, 5]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [2, 1], [3, 3], [4, 4], [5, 5]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],target = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],target = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, 1000], [1001, 1001], [999, 999], [998, 998]],target = [1002, 1002]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, 1000], [1001, 1001], [999, 999], [998, 998]],target = [1002, 1002]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1000, -1000], [-2000, -2000], [-1500, -1500], [-500, -500]],target = [-1500, -1500]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1000, -1000], [-2000, -2000], [-1500, -1500], [-500, -500]],target = [-1500, -1500]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-5000, 5000], [5000, -5000], [0, 0], [1, 1]],target = [5000, 5000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-5000, 5000], [5000, -5000], [0, 0], [1, 1]],target = [5000, 5000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, 1000], [2000, 2000], [3000, 3000]],target = [1500, 1500]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, 1000], [2000, 2000], [3000, 3000]],target = [1500, 1500]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],target = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],target = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, -20], [-30, -40], [-50, -60]],target = [-40, -50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, -20], [-30, -40], [-50, -60]],target = [-40, -50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-5, 5], [5, -5], [-10, 10], [10, -10]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-5, 5], [5, -5], [-10, 10], [10, -10]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-100, -100], [100, 100], [-50, 50], [50, -50]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-100, -100], [100, 100], [-50, 50], [50, -50]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10000, -10000], [10000, 10000]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10000, -10000], [10000, 10000]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 1], [-2, 2], [-3, 3], [-4, 4]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 1], [-2, 2], [-3, 3], [-4, 4]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, 1000], [999, 1000], [1000, 999], [999, 999]],target = [1001, 1001]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, 1000], [999, 1000], [1000, 999], [999, 999]],target = [1001, 1001]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, -1], [-1, 1], [-1, -1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, -1], [-1, 1], [-1, -1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 0], [0, 100], [50, 50], [0, 0]],target = [50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 0], [0, 100], [50, 50], [0, 0]],target = [50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],target = [0, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],target = [0, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, -1000], [-1000, 1000]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, -1000], [-1000, 1000]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 1], [1, 0], [1, 1]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 1], [1, 0], [1, 1]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[2, 2], [3, 3], [4, 4], [5, 5]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[2, 2], [3, 3], [4, 4], [5, 5]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1000, 1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1000, 1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-50, -50], [-49, -49], [-48, -48], [-47, -47]],target = [-45, -45]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-50, -50], [-49, -49], [-48, -48], [-47, -47]],target = [-45, -45]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1000, -1000], [-1001, -1001], [-1002, -1002]],target = [-1003, -1003]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1000, -1000], [-1001, -1001], [-1002, -1002]],target = [-1003, -1003]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 10000], [10000, 0], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 10000], [10000, 0], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],target = [6, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],target = [6, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10000, 0], [0, -10000], [10000, 0], [0, 10000]],target = [1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10000, 0], [0, -10000], [10000, 0], [0, 10000]],target = [1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],target = [5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],target = [5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, 10], [10, -10]],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, 10], [10, -10]],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 1], [0, 0], [0, 2], [2, 0]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 1], [0, 0], [0, 2], [2, 0]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[2, 3], [4, 5], [6, 7], [8, 9]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[2, 3], [4, 5], [6, 7], [8, 9]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [-5, -5], [5, -5], [-5, 5]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [-5, -5], [5, -5], [-5, 5]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-100, -100], [100, 100]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-100, -100], [100, 100]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]],target = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]],target = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],target = [60, 60]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],target = [60, 60]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-100, 0], [0, -100], [100, 0], [0, 100]],target = [100, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-100, 0], [0, -100], [100, 0], [0, 100]],target = [100, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 0], [100, 0], [100, 0]],target = [200, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 0], [100, 0], [100, 0]],target = [200, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-5, 0], [5, 0], [0, -5], [0, 5]],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-5, 0], [5, 0], [0, -5], [0, 5]],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 1], [1, -1], [-1, -1]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 1], [1, -1], [-1, -1]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, 1000], [2000, 2000], [1500, 1500], [500, 500]],target = [1500, 1500]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, 1000], [2000, 2000], [1500, 1500], [500, 500]],target = [1500, 1500]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]],target = [3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]],target = [3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],target = [0, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],target = [0, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6]],target = [-5, -5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6]],target = [-5, -5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-100, -100], [-200, -200], [-300, -300]],target = [-150, -150]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-100, -100], [-200, -200], [-300, -300]],target = [-150, -150]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[5, 5], [5, 5], [5, 5]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[5, 5], [5, 5], [5, 5]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 1], [0, 0], [2, 2], [3, 3]],target = [2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 1], [0, 0], [2, 2], [3, 3]],target = [2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-5, -5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-5, -5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-1, 0], [0, -1]],target = [-10000, -10000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-1, 0], [0, -1]],target = [-10000, -10000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[1000, 1000], [1001, 1001], [1002, 1002]],target = [1003, 1003]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[1000, 1000], [1001, 1001], [1002, 1002]],target = [1003, 1003]) == False: {e}')
    
    total += 1
    try:
        result = candidate(ghosts = [[-10, -10], [-20, -20], [-30, -30], [-40, -40]],target = [-15, -15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ghosts = [[-10, -10], [-20, -20], [-30, -30], [-40, -40]],target = [-15, -15]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(ghosts = [[0, 0], [0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[-1, -1]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [4, 4]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4]],target = [5, 5]) == False
    assert candidate(ghosts = [[1, 0], [0, 3]],target = [0, 1]) == True
    assert candidate(ghosts = [[-1, -1], [-2, -2]],target = [-3, -3]) == False
    assert candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False
    assert candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [0, 0]) == True
    assert candidate(ghosts = [[-10000, -10000]],target = [-9999, -9999]) == False
    assert candidate(ghosts = [[100, 100]],target = [-100, -100]) == True
    assert candidate(ghosts = [[10000, 10000]],target = [-10000, -10000]) == True
    assert candidate(ghosts = [[10000, 10000], [-10000, -10000]],target = [5000, 5000]) == False
    assert candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[0, 0]],target = [0, 0]) == False
    assert candidate(ghosts = [[100, 100], [99, 100], [100, 99]],target = [101, 101]) == False
    assert candidate(ghosts = [[5, 5], [5, 6], [6, 5], [6, 6]],target = [5, 5]) == False
    assert candidate(ghosts = [[0, 1], [1, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[2, 0]],target = [1, 0]) == False
    assert candidate(ghosts = [[0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 1], [2, 2]],target = [3, 3]) == False
    assert candidate(ghosts = [[-1, -1]],target = [-2, -2]) == False
    assert candidate(ghosts = [[1, 1], [1, 1]],target = [2, 2]) == False
    assert candidate(ghosts = [[10000, 10000]],target = [9999, 9999]) == False
    assert candidate(ghosts = [[-1, -1], [2, 2]],target = [0, 0]) == True
    assert candidate(ghosts = [[-2, -2], [-3, -3]],target = [-4, -4]) == False
    assert candidate(ghosts = [[-1, 0], [0, -1]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 0]],target = [2, 0]) == False
    assert candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 0], [0, 1], [1, 1]],target = [-1, -1]) == True
    assert candidate(ghosts = [[-5, 5], [5, -5], [0, 10]],target = [5, 5]) == False
    assert candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0]],target = [0, 0]) == True
    assert candidate(ghosts = [[5, 5], [3, 3], [-1, -1]],target = [0, 0]) == True
    assert candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [1001, 1001]) == False
    assert candidate(ghosts = [[-1, -2], [-2, -3], [-3, -4], [-4, -5], [-5, -6], [-6, -7]],target = [-7, -8]) == False
    assert candidate(ghosts = [[1, 0], [0, 1]],target = [-1, -1]) == True
    assert candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False
    assert candidate(ghosts = [[0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[-100, 100], [100, -100], [50, 50]],target = [0, 0]) == True
    assert candidate(ghosts = [[10, 10], [10, -10], [-10, 10], [-10, -10]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],target = [2, 5]) == False
    assert candidate(ghosts = [[-1, -1], [1, 1]],target = [10000, 10000]) == False
    assert candidate(ghosts = [[10000, 0], [0, 10000], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-1, -1]) == False
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [5, 5]) == True
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [-1, -2]) == True
    assert candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [2, 2]) == False
    assert candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],target = [9, 10]) == False
    assert candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],target = [6, 7]) == False
    assert candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [-2, 0], [0, -2], [2, 0], [0, 2]],target = [3, 3]) == False
    assert candidate(ghosts = [[-1, -1], [-1, 1], [1, -1], [1, 1]],target = [2, 2]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],target = [0, 0]) == True
    assert candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False
    assert candidate(ghosts = [[-10, 10], [10, -10], [-10, -10]],target = [0, 0]) == True
    assert candidate(ghosts = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]],target = [10, 10]) == False
    assert candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True
    assert candidate(ghosts = [[-10, 0], [0, -10], [10, 0], [0, 10]],target = [3, 3]) == True
    assert candidate(ghosts = [[-10000, -10000], [-10000, 10000], [10000, -10000], [10000, 10000]],target = [0, 0]) == True
    assert candidate(ghosts = [[5, -5], [-5, 5], [0, 0]],target = [-3, 3]) == False
    assert candidate(ghosts = [[1, 2], [2, 1], [3, 3], [4, 4], [5, 5]],target = [0, 0]) == True
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],target = [6, 6]) == False
    assert candidate(ghosts = [[1000, 1000], [1001, 1001], [999, 999], [998, 998]],target = [1002, 1002]) == False
    assert candidate(ghosts = [[-1000, -1000], [-2000, -2000], [-1500, -1500], [-500, -500]],target = [-1500, -1500]) == False
    assert candidate(ghosts = [[-5000, 5000], [5000, -5000], [0, 0], [1, 1]],target = [5000, 5000]) == False
    assert candidate(ghosts = [[1000, 1000], [2000, 2000], [3000, 3000]],target = [1500, 1500]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],target = [6, 6]) == False
    assert candidate(ghosts = [[-10, -20], [-30, -40], [-50, -60]],target = [-40, -50]) == False
    assert candidate(ghosts = [[-5, 5], [5, -5], [-10, 10], [10, -10]],target = [0, 0]) == True
    assert candidate(ghosts = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]],target = [2, 2]) == False
    assert candidate(ghosts = [[-100, -100], [100, 100], [-50, 50], [50, -50]],target = [0, 0]) == True
    assert candidate(ghosts = [[10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]],target = [0, 0]) == True
    assert candidate(ghosts = [[-10000, -10000], [10000, 10000]],target = [0, 0]) == True
    assert candidate(ghosts = [[-1, 1], [-2, 2], [-3, 3], [-4, 4]],target = [0, 0]) == True
    assert candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [15, 15]) == False
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [7, 8]) == False
    assert candidate(ghosts = [[0, 0], [0, 0]],target = [0, 0]) == False
    assert candidate(ghosts = [[1000, 1000], [999, 1000], [1000, 999], [999, 999]],target = [1001, 1001]) == False
    assert candidate(ghosts = [[1, 1], [1, -1], [-1, 1], [-1, -1]],target = [2, 2]) == False
    assert candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [0, 0]) == True
    assert candidate(ghosts = [[100, 0], [0, 100], [50, 50], [0, 0]],target = [50, 50]) == False
    assert candidate(ghosts = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],target = [0, 5]) == False
    assert candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [7, 8]) == False
    assert candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],target = [10, 10]) == False
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False
    assert candidate(ghosts = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False
    assert candidate(ghosts = [[1000, -1000], [-1000, 1000]],target = [0, 0]) == True
    assert candidate(ghosts = [[0, 0], [0, 1], [1, 0], [1, 1]],target = [10, 10]) == False
    assert candidate(ghosts = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],target = [0, 0]) == True
    assert candidate(ghosts = [[2, 2], [3, 3], [4, 4], [5, 5]],target = [1, 1]) == False
    assert candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1000, 1000]) == False
    assert candidate(ghosts = [[-50, -50], [-49, -49], [-48, -48], [-47, -47]],target = [-45, -45]) == False
    assert candidate(ghosts = [[-1000, -1000], [-1001, -1001], [-1002, -1002]],target = [-1003, -1003]) == False
    assert candidate(ghosts = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],target = [0, 0]) == True
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4]],target = [0, 0]) == True
    assert candidate(ghosts = [[0, 10000], [10000, 0], [-10000, 0], [0, -10000]],target = [5000, 5000]) == False
    assert candidate(ghosts = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],target = [6, 0]) == False
    assert candidate(ghosts = [[-10000, 0], [0, -10000], [10000, 0], [0, 10000]],target = [1, 1]) == True
    assert candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False
    assert candidate(ghosts = [[10, 10], [20, 20], [30, 30]],target = [0, 0]) == True
    assert candidate(ghosts = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],target = [5, 6]) == False
    assert candidate(ghosts = [[-10, 10], [10, -10]],target = [5, 5]) == True
    assert candidate(ghosts = [[5, 5], [5, -5], [-5, 5], [-5, -5]],target = [10, 10]) == False
    assert candidate(ghosts = [[1, 0], [0, 1], [0, 0], [0, 2], [2, 0]],target = [2, 2]) == False
    assert candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [2, 2]) == False
    assert candidate(ghosts = [[2, 3], [4, 5], [6, 7], [8, 9]],target = [10, 10]) == False
    assert candidate(ghosts = [[5, 5], [-5, -5], [5, -5], [-5, 5]],target = [0, 0]) == True
    assert candidate(ghosts = [[-100, -100], [100, 100]],target = [0, 0]) == True
    assert candidate(ghosts = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]],target = [0, 0]) == False
    assert candidate(ghosts = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],target = [60, 60]) == False
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8]],target = [4, 4]) == False
    assert candidate(ghosts = [[-100, 0], [0, -100], [100, 0], [0, 100]],target = [100, 100]) == False
    assert candidate(ghosts = [[100, 0], [100, 0], [100, 0]],target = [200, 0]) == False
    assert candidate(ghosts = [[-5, 0], [5, 0], [0, -5], [0, 5]],target = [3, 3]) == False
    assert candidate(ghosts = [[-1, 1], [1, -1], [-1, -1]],target = [1, 1]) == False
    assert candidate(ghosts = [[1000, 1000], [2000, 2000], [1500, 1500], [500, 500]],target = [1500, 1500]) == False
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6]],target = [3, 3]) == False
    assert candidate(ghosts = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]],target = [3, 1]) == False
    assert candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[100, 0], [0, 100], [-100, 0], [0, -100]],target = [50, 50]) == False
    assert candidate(ghosts = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],target = [0, 6]) == False
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]],target = [-6, -6]) == False
    assert candidate(ghosts = [[-1000, 0], [0, -1000], [1000, 0], [0, 1000]],target = [0, 0]) == True
    assert candidate(ghosts = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6]],target = [-5, -5]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [5, 5]) == False
    assert candidate(ghosts = [[-100, -100], [-200, -200], [-300, -300]],target = [-150, -150]) == False
    assert candidate(ghosts = [[5, 5], [5, 5], [5, 5]],target = [10, 10]) == False
    assert candidate(ghosts = [[1, 0], [0, 1], [0, 0], [2, 2], [3, 3]],target = [2, 1]) == False
    assert candidate(ghosts = [[0, 0], [0, 0], [0, 0], [0, 0]],target = [1, 1]) == False
    assert candidate(ghosts = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]],target = [-5, -5]) == False
    assert candidate(ghosts = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]],target = [1, 1]) == False
    assert candidate(ghosts = [[0, 1], [1, 0], [0, -1], [-1, 0]],target = [10, 10]) == False
    assert candidate(ghosts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],target = [1, 1]) == False
    assert candidate(ghosts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = [0, 0]) == True
    assert candidate(ghosts = [[-1, 0], [0, -1]],target = [-10000, -10000]) == False
    assert candidate(ghosts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],target = [2, 2]) == False
    assert candidate(ghosts = [[1000, 1000], [1001, 1001], [1002, 1002]],target = [1003, 1003]) == False
    assert candidate(ghosts = [[-10, -10], [-20, -20], [-30, -30], [-40, -40]],target = [-15, -15]) == False


