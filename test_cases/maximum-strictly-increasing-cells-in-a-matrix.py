def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-100000, 100000], [-100000, 100000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-100000, 100000], [-100000, 100000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 9, 8, 7, 6], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 9, 8, 7, 6], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 1], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 1], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 9, 8, 7], [6, 5, 4, 3], [2, 1, 0, -1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 9, 8, 7], [6, 5, 4, 3], [2, 1, 0, -1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1], [1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1], [1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 1, 6], [-9, 5, 7]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 1, 6], [-9, 5, 7]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 10, 3, 4, 5], [10, 1, 8, 7, 6], [3, 8, 1, 14, 15], [18, 7, 14, 1, 16]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 10, 3, 4, 5], [10, 1, 8, 7, 6], [3, 8, 1, 14, 15], [18, 7, 14, 1, 16]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [30, 20, 10], [10, 20, 30], [30, 20, 10], [10, 20, 30]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [30, 20, 10], [10, 20, 30], [30, 20, 10], [10, 20, 30]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-5, -4, -3, -2, -1], [-4, -3, -2, -1, 0], [-3, -2, -1, 0, 1], [-2, -1, 0, 1, 2], [-1, 0, 1, 2, 3]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-5, -4, -3, -2, -1], [-4, -3, -2, -1, 0], [-3, -2, -1, 0, 1], [-2, -1, 0, 1, 2], [-1, 0, 1, 2, 3]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3, -4], [-4, -3, -2, -1], [-5, -6, -7, -8], [-8, -7, -6, -5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3, -4], [-4, -3, -2, -1], [-5, -6, -7, -8], [-8, -7, -6, -5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 99, 98, 97, 96], [95, 94, 93, 92, 91], [90, 89, 88, 87, 86], [85, 84, 83, 82, 81], [80, 79, 78, 77, 76]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 99, 98, 97, 96], [95, 94, 93, 92, 91], [90, 89, 88, 87, 86], [85, 84, 83, 82, 81], [80, 79, 78, 77, 76]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-10, -9, -8, -7], [-6, -5, -4, -3], [-2, -1, 0, 1], [2, 3, 4, 5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-10, -9, -8, -7], [-6, -5, -4, -3], [-2, -1, 0, 1], [2, 3, 4, 5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 2, 3, 1], [1, 3, 1, 1], [1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 2, 3, 1], [1, 3, 1, 1], [1, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, 0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, 0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 3, 1, 4], [6, 2, 8, 7], [9, 11, 13, 12], [10, 15, 14, 16]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 3, 1, 4], [6, 2, 8, 7], [9, 11, 13, 12], [10, 15, 14, 16]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 10, 3, 11, 5], [12, 6, 7, 8, 9], [13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 10, 3, 11, 5], [12, 6, 7, 8, 9], [13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 3, 8, 2, 9], [1, 6, 4, 7, 3], [9, 1, 8, 2, 5], [2, 7, 3, 8, 4], [8, 2, 9, 4, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 3, 8, 2, 9], [1, 6, 4, 7, 3], [9, 1, 8, 2, 5], [2, 7, 3, 8, 4], [8, 2, 9, 4, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [9, 7, 5, 3, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [9, 7, 5, 3, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-10, -20, -30], [-20, -30, -40], [-30, -40, -50]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-10, -20, -30], [-20, -30, -40], [-30, -40, -50]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 2, 4, 5], [6, 5, 4, 3, 2], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 2, 4, 5], [6, 5, 4, 3, 2], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 5, 1, 5], [5, 1, 10, 1, 5], [5, 1, 5, 1, 5], [5, 5, 5, 5, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 5, 1, 5], [5, 1, 10, 1, 5], [5, 1, 5, 1, 5], [5, 5, 5, 5, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 2, 4, 5], [6, 8, 7, 9, 10], [11, 13, 12, 15, 14], [19, 18, 17, 20, 21], [22, 23, 24, 25, 26]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 2, 4, 5], [6, 8, 7, 9, 10], [11, 13, 12, 15, 14], [19, 18, 17, 20, 21], [22, 23, 24, 25, 26]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 2, 1], [1, 2, 2, 2, 1], [1, 1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 2, 1], [1, 2, 2, 2, 1], [1, 1, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 2, 3, 5], [5, 4, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 2, 3, 5], [5, 4, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 1, 4, 1, 5], [9, 2, 6, 5, 3], [5, 8, 9, 7, 9], [3, 2, 3, 8, 4]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 1, 4, 1, 5], [9, 2, 6, 5, 3], [5, 8, 9, 7, 9], [3, 2, 3, 8, 4]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 3, 1], [1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 3, 1], [1, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [12, 10, 8, 6, 4, 2]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [12, 10, 8, 6, 4, 2]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 8, 9, 7, 9, 3], [2, 8, 0, 3, 1, 4]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 8, 9, 7, 9, 3], [2, 8, 0, 3, 1, 4]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65], [70, 75, 80]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65], [70, 75, 80]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 100, 2, 99, 3, 98, 4, 97, 5, 96], [6, 95, 7, 94, 8, 93, 9, 92, 10, 91]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 100, 2, 99, 3, 98, 4, 97, 5, 96], [6, 95, 7, 94, 8, 93, 9, 92, 10, 91]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 100, 1], [100, 1, 100], [1, 100, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 100, 1], [100, 1, 100], [1, 100, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 2, 3, 4, 1], [1, 2, 6, 7, 8], [3, 4, 5, 6, 9], [9, 8, 7, 6, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 2, 3, 4, 1], [1, 2, 6, 7, 8], [3, 4, 5, 6, 9], [9, 8, 7, 6, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-10, -20, -30], [-30, -20, -10], [-10, -30, -20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-10, -20, -30], [-30, -20, -10], [-10, -30, -20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-10, -20, -30, -40], [-40, -30, -20, -10], [-50, -60, -70, -80], [-80, -70, -60, -50]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-10, -20, -30, -40], [-40, -30, -20, -10], [-50, -60, -70, -80], [-80, -70, -60, -50]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 5, 3, 6, 2], [9, 8, 7, 10, 11], [4, 13, 12, 15, 14], [19, 18, 17, 20, 21]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 5, 3, 6, 2], [9, 8, 7, 10, 11], [4, 13, 12, 15, 14], [19, 18, 17, 20, 21]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 3, 1, 2], [4, 6, 2, 3], [7, 5, 3, 4], [8, 6, 4, 5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 3, 1, 2], [4, 6, 2, 3], [7, 5, 3, 4], [8, 6, 4, 5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-10, -20, -30, -40], [-35, -25, -15, -5], [-50, -45, -40, -35], [-60, -55, -50, -45]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-10, -20, -30, -40], [-35, -25, -15, -5], [-50, -45, -40, -35], [-60, -55, -50, -45]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11], [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11], [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1000, 2, 999], [3, 998, 4, 997], [5, 996, 6, 995], [7, 994, 8, 993]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1000, 2, 999], [3, 998, 4, 997], [5, 996, 6, 995], [7, 994, 8, 993]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 3, 9, 1], [1, 7, 6, 8], [2, 9, 5, 1], [8, 5, 4, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 3, 9, 1], [1, 7, 6, 8], [2, 9, 5, 1], [8, 5, 4, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3], [-3, -2, -1], [1, 0, -1], [-2, -3, -4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3], [-3, -2, -1], [1, 0, -1], [-2, -3, -4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, -100, 200, -200, 300], [-300, 300, -400, 400, -500], [500, -500, 600, -600, 700]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, -100, 200, -200, 300], [-300, 300, -400, 400, -500], [500, -500, 600, -600, 700]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, -100, 200, -200, 300], [-100, 200, -200, 300, -300], [200, -200, 300, -300, 400], [0, 0, 0, 0, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, -100, 200, -200, 300], [-100, 200, -200, 300, -300], [200, -200, 300, -300, 400], [0, 0, 0, 0, 0]]) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40]]) == 5
    assert candidate(mat = [[1]]) == 1
    assert candidate(mat = [[-100000, 100000], [-100000, 100000]]) == 2
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
    assert candidate(mat = [[10, 9, 8, 7, 6], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]]) == 10
    assert candidate(mat = [[3, 1], [3, 4]]) == 2
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 6
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9]]) == 6
    assert candidate(mat = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 5
    assert candidate(mat = [[10, 9, 8, 7], [6, 5, 4, 3], [2, 1, 0, -1]]) == 6
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5
    assert candidate(mat = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 5
    assert candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 5
    assert candidate(mat = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 6
    assert candidate(mat = [[1, 1], [1, 1]]) == 1
    assert candidate(mat = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]) == 5
    assert candidate(mat = [[10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 1, 1]]) == 6
    assert candidate(mat = [[3, 1, 6], [-9, 5, 7]]) == 4
    assert candidate(mat = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]) == 6
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]]) == 21
    assert candidate(mat = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 8
    assert candidate(mat = [[1, 10, 3, 4, 5], [10, 1, 8, 7, 6], [3, 8, 1, 14, 15], [18, 7, 14, 1, 16]]) == 10
    assert candidate(mat = [[10, 20, 30], [30, 20, 10], [10, 20, 30], [30, 20, 10], [10, 20, 30]]) == 3
    assert candidate(mat = [[-5, -4, -3, -2, -1], [-4, -3, -2, -1, 0], [-3, -2, -1, 0, 1], [-2, -1, 0, 1, 2], [-1, 0, 1, 2, 3]]) == 9
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]) == 16
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]]) == 12
    assert candidate(mat = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]]) == 14
    assert candidate(mat = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) == 7
    assert candidate(mat = [[-1, -2, -3, -4], [-4, -3, -2, -1], [-5, -6, -7, -8], [-8, -7, -6, -5]]) == 8
    assert candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == 13
    assert candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5
    assert candidate(mat = [[100, 99, 98, 97, 96], [95, 94, 93, 92, 91], [90, 89, 88, 87, 86], [85, 84, 83, 82, 81], [80, 79, 78, 77, 76]]) == 9
    assert candidate(mat = [[100, 200, 300], [150, 250, 350], [200, 300, 400]]) == 5
    assert candidate(mat = [[1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10], [10, 1, 10, 1, 10, 1], [1, 10, 1, 10, 1, 10]]) == 2
    assert candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2
    assert candidate(mat = [[-10, -9, -8, -7], [-6, -5, -4, -3], [-2, -1, 0, 1], [2, 3, 4, 5]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == 12
    assert candidate(mat = [[1, 1, 1, 1], [1, 2, 3, 1], [1, 3, 1, 1], [1, 1, 1, 1]]) == 3
    assert candidate(mat = [[-1, 0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 9
    assert candidate(mat = [[5, 3, 1, 4], [6, 2, 8, 7], [9, 11, 13, 12], [10, 15, 14, 16]]) == 12
    assert candidate(mat = [[1, 10, 3, 11, 5], [12, 6, 7, 8, 9], [13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]) == 12
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 7
    assert candidate(mat = [[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]]) == 1
    assert candidate(mat = [[5, 3, 8, 2, 9], [1, 6, 4, 7, 3], [9, 1, 8, 2, 5], [2, 7, 3, 8, 4], [8, 2, 9, 4, 1]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]]) == 8
    assert candidate(mat = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [9, 7, 5, 3, 1]]) == 7
    assert candidate(mat = [[-10, -20, -30], [-20, -30, -40], [-30, -40, -50]]) == 5
    assert candidate(mat = [[1, 3, 2, 4, 5], [6, 5, 4, 3, 2], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16]]) == 11
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12]]) == 9
    assert candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 5, 1, 5], [5, 1, 10, 1, 5], [5, 1, 5, 1, 5], [5, 5, 5, 5, 5]]) == 3
    assert candidate(mat = [[1, 3, 2, 4, 5], [6, 8, 7, 9, 10], [11, 13, 12, 15, 14], [19, 18, 17, 20, 21], [22, 23, 24, 25, 26]]) == 12
    assert candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 2, 1], [1, 2, 2, 2, 1], [1, 1, 1, 1, 1]]) == 3
    assert candidate(mat = [[5, 5, 5, 5, 5], [5, 1, 2, 3, 5], [5, 4, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 4
    assert candidate(mat = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
    assert candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == 10
    assert candidate(mat = [[3, 1, 4, 1, 5], [9, 2, 6, 5, 3], [5, 8, 9, 7, 9], [3, 2, 3, 8, 4]]) == 7
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 3
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 100]]) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]]) == 17
    assert candidate(mat = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 3, 1], [1, 1, 1, 1]]) == 3
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [12, 10, 8, 6, 4, 2]]) == 8
    assert candidate(mat = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) == 3
    assert candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7
    assert candidate(mat = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 8, 9, 7, 9, 3], [2, 8, 0, 3, 1, 4]]) == 9
    assert candidate(mat = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65], [70, 75, 80]]) == 7
    assert candidate(mat = [[1, 100, 2, 99, 3, 98, 4, 97, 5, 96], [6, 95, 7, 94, 8, 93, 9, 92, 10, 91]]) == 12
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == 12
    assert candidate(mat = [[1, 100, 1], [100, 1, 100], [1, 100, 1]]) == 2
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]]) == 9
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]) == 10
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 14
    assert candidate(mat = [[5, 2, 3, 4, 1], [1, 2, 6, 7, 8], [3, 4, 5, 6, 9], [9, 8, 7, 6, 5]]) == 8
    assert candidate(mat = [[-10, -20, -30], [-30, -20, -10], [-10, -30, -20]]) == 3
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]]) == 10
    assert candidate(mat = [[-10, -20, -30, -40], [-40, -30, -20, -10], [-50, -60, -70, -80], [-80, -70, -60, -50]]) == 8
    assert candidate(mat = [[1, 5, 3, 6, 2], [9, 8, 7, 10, 11], [4, 13, 12, 15, 14], [19, 18, 17, 20, 21]]) == 12
    assert candidate(mat = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 7
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 5
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]]) == 6
    assert candidate(mat = [[5, 3, 1, 2], [4, 6, 2, 3], [7, 5, 3, 4], [8, 6, 4, 5]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 5
    assert candidate(mat = [[10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]]) == 7
    assert candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 7
    assert candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16]]) == 20
    assert candidate(mat = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]) == 6
    assert candidate(mat = [[-10, -20, -30, -40], [-35, -25, -15, -5], [-50, -45, -40, -35], [-60, -55, -50, -45]]) == 8
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11], [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]]) == 21
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == 8
    assert candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25]]) == 25
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) == 5
    assert candidate(mat = [[1, 1000, 2, 999], [3, 998, 4, 997], [5, 996, 6, 995], [7, 994, 8, 993]]) == 10
    assert candidate(mat = [[5, 3, 9, 1], [1, 7, 6, 8], [2, 9, 5, 1], [8, 5, 4, 6]]) == 6
    assert candidate(mat = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]) == 26
    assert candidate(mat = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 11
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]) == 14
    assert candidate(mat = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]]) == 4
    assert candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]) == 2
    assert candidate(mat = [[-1, -2, -3], [-3, -2, -1], [1, 0, -1], [-2, -3, -4]]) == 5
    assert candidate(mat = [[100, -100, 200, -200, 300], [-300, 300, -400, 400, -500], [500, -500, 600, -600, 700]]) == 7
    assert candidate(mat = [[100, -100, 200, -200, 300], [-100, 200, -200, 300, -300], [200, -200, 300, -300, 400], [0, 0, 0, 0, 0]]) == 8


