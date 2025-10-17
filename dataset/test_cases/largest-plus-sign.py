def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 6], [2, 0], [2, 6], [3, 0], [3, 6], [4, 0], [4, 6], [5, 0], [5, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 6], [2, 0], [2, 6], [3, 0], [3, 6], [4, 0], [4, 6], [5, 0], [5, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,mines = [[0, 0], [0, 3], [3, 0], [3, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,mines = [[0, 0], [0, 3], [3, 0], [3, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,mines = [[1, 1], [1, 3], [3, 1], [3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,mines = [[1, 1], [1, 3], [3, 1], [3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,mines = [[0, 0], [0, 4], [4, 0], [4, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,mines = [[0, 0], [0, 4], [4, 0], [4, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,mines = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,mines = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,mines = [[0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,mines = [[0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,mines = [[0, 0], [3, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,mines = [[0, 0], [3, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,mines = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,mines = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,mines = [[1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,mines = [[1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,mines = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,mines = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = []) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = []) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,mines = []) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,mines = []) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,mines = [[4, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,mines = [[4, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,mines = [[0, 0], [1, 1], [2, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,mines = [[0, 0], [1, 1], [2, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,mines = []) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,mines = []) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,mines = [[1, 2], [2, 1], [2, 3], [3, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,mines = [[1, 2], [2, 1], [2, 3], [3, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,mines = [[50, 50], [49, 49], [49, 51], [51, 49], [51, 51], [49, 50], [50, 49], [50, 51], [60, 60], [30, 30]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,mines = [[50, 50], [49, 49], [49, 51], [51, 49], [51, 51], [49, 50], [50, 49], [50, 51], [60, 60], [30, 30]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [14, 14]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [14, 14]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253]]) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253]]) == 247: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,mines = [[10, 10], [11, 11], [12, 12], [13, 13], [10, 12], [12, 10], [11, 9], [11, 13], [9, 11], [13, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,mines = [[10, 10], [11, 11], [12, 12], [13, 13], [10, 12], [12, 10], [11, 9], [11, 13], [9, 11], [13, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[0, 0], [9, 9], [0, 9], [9, 0], [4, 4], [5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[0, 0], [9, 9], [0, 9], [9, 0], [4, 4], [5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[5, 5], [5, 6], [6, 5], [4, 5], [5, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[5, 5], [5, 6], [6, 5], [4, 5], [5, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,mines = [[37, 37], [36, 36], [36, 38], [38, 36], [38, 38], [36, 37], [37, 36], [37, 38]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,mines = [[37, 37], [36, 36], [36, 38], [38, 36], [38, 38], [36, 37], [37, 36], [37, 38]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,mines = [[10, 10], [11, 10], [9, 10], [10, 9], [10, 11], [15, 15], [14, 15], [16, 15], [15, 14], [15, 16], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,mines = [[10, 10], [11, 10], [9, 10], [10, 9], [10, 11], [15, 15], [14, 15], [16, 15], [15, 14], [15, 16], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[5, 5], [5, 14], [14, 5], [14, 14], [10, 10], [10, 9], [9, 10], [9, 9], [10, 8], [8, 10], [0, 0], [19, 19]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[5, 5], [5, 14], [14, 5], [14, 14], [10, 10], [10, 9], [9, 10], [9, 9], [10, 8], [8, 10], [0, 0], [19, 19]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [249, 249], [249, 251], [251, 249], [251, 251], [249, 250], [250, 249], [250, 251], [200, 200], [300, 300]]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [249, 249], [249, 251], [251, 249], [251, 251], [249, 250], [250, 249], [250, 251], [200, 200], [300, 300]]) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,mines = [[50, 50], [49, 49], [51, 51], [48, 48], [52, 52], [47, 47], [53, 53], [46, 46], [54, 54], [45, 45], [55, 55]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,mines = [[50, 50], [49, 49], [51, 51], [48, 48], [52, 52], [47, 47], [53, 53], [46, 46], [54, 54], [45, 45], [55, 55]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [250, 251], [250, 249], [249, 250], [251, 250]]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [250, 251], [250, 249], [249, 250], [251, 250]]) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,mines = [[0, 0], [11, 11], [5, 5], [6, 5], [5, 6], [6, 6], [7, 7], [8, 8], [4, 4], [4, 3], [4, 2], [3, 4], [2, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,mines = [[0, 0], [11, 11], [5, 5], [6, 5], [5, 6], [6, 6], [7, 7], [8, 8], [4, 4], [4, 3], [4, 2], [3, 4], [2, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,mines = [[0, 0], [0, 1], [0, 2], [0, 22], [0, 23], [0, 24], [1, 0], [1, 24], [2, 0], [2, 24], [22, 0], [22, 24], [23, 0], [23, 24], [24, 0], [24, 1], [24, 2], [24, 22], [24, 23], [24, 24]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,mines = [[0, 0], [0, 1], [0, 2], [0, 22], [0, 23], [0, 24], [1, 0], [1, 24], [2, 0], [2, 24], [22, 0], [22, 24], [23, 0], [23, 24], [24, 0], [24, 1], [24, 2], [24, 22], [24, 23], [24, 24]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[1, 1], [1, 18], [18, 1], [18, 18], [9, 9], [10, 10], [11, 11]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[1, 1], [1, 18], [18, 1], [18, 18], [9, 9], [10, 10], [11, 11]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 4], [4, 5], [5, 6], [6, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 4], [4, 5], [5, 6], [6, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 12], [12, 10], [12, 11], [12, 12]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 12], [12, 10], [12, 11], [12, 12]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,mines = [[100, 100], [100, 101], [101, 100], [99, 99], [101, 99], [99, 101], [98, 98], [102, 102]]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,mines = [[100, 100], [100, 101], [101, 100], [99, 99], [101, 99], [99, 101], [98, 98], [102, 102]]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 9], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 9], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [7, 9], [8, 9], [9, 7], [9, 8], [9, 9]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [7, 9], [8, 9], [9, 7], [9, 8], [9, 9]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[0, 5], [5, 0], [5, 5], [9, 5], [5, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[0, 5], [5, 0], [5, 5], [9, 5], [5, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [6, 8], [6, 9], [7, 6], [7, 9], [8, 6], [8, 9], [9, 6], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 10], [7, 5], [7, 10], [8, 5], [8, 10], [9, 5], [9, 10], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [6, 8], [6, 9], [7, 6], [7, 9], [8, 6], [8, 9], [9, 6], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 10], [7, 5], [7, 10], [8, 5], [8, 10], [9, 5], [9, 10], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,mines = [[12, 12], [11, 11], [13, 13], [10, 10], [11, 10], [10, 11], [13, 12], [12, 11], [11, 13], [12, 13], [13, 11], [10, 12], [12, 10], [12, 14], [14, 12], [11, 12], [13, 12], [12, 11], [12, 13]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,mines = [[12, 12], [11, 11], [13, 13], [10, 10], [11, 10], [10, 11], [13, 12], [12, 11], [11, 13], [12, 13], [13, 11], [10, 12], [12, 10], [12, 14], [14, 12], [11, 12], [13, 12], [12, 11], [12, 13]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 6], [6, 5], [5, 4], [4, 5], [3, 3], [7, 7], [2, 2], [8, 8], [1, 1], [9, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 6], [6, 5], [5, 4], [4, 5], [3, 3], [7, 7], [2, 2], [8, 8], [1, 1], [9, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,mines = [[5, 5], [5, 19], [19, 5], [19, 19], [12, 12], [13, 13], [12, 13], [13, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,mines = [[5, 5], [5, 19], [19, 5], [19, 19], [12, 12], [13, 13], [12, 13], [13, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [4, 2], [5, 2], [6, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [4, 2], [5, 2], [6, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,mines = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,mines = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 4], [6, 5], [6, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 4], [6, 5], [6, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,mines = [[15, 15], [14, 14], [13, 13], [12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,mines = [[15, 15], [14, 14], [13, 13], [12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,mines = [[1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,mines = [[1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,mines = [[150, 150], [149, 149], [149, 151], [151, 149], [151, 151], [149, 150], [150, 149], [150, 151], [100, 100], [200, 200]]) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,mines = [[150, 150], [149, 149], [149, 151], [151, 149], [151, 151], [149, 150], [150, 149], [150, 151], [100, 100], [200, 200]]) == 149: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[10, 10], [10, 11], [11, 10], [11, 11], [9, 9], [9, 10], [9, 11], [10, 9], [11, 9], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [9, 8], [9, 12], [10, 8], [10, 12], [11, 8], [11, 12], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [8, 7], [8, 13], [9, 7], [9, 13], [10, 7], [10, 13], [11, 7], [11, 13], [12, 7], [12, 13], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[10, 10], [10, 11], [11, 10], [11, 11], [9, 9], [9, 10], [9, 11], [10, 9], [11, 9], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [9, 8], [9, 12], [10, 8], [10, 12], [11, 8], [11, 12], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [8, 7], [8, 13], [9, 7], [9, 13], [10, 7], [10, 13], [11, 7], [11, 13], [12, 7], [12, 13], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1], [10, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1], [10, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,mines = [[25, 25], [25, 24], [25, 23], [25, 22], [25, 21], [25, 20], [25, 19], [25, 18], [25, 17], [25, 16], [25, 15], [25, 14], [25, 13], [25, 12], [25, 11], [25, 10], [25, 9], [25, 8], [25, 7], [25, 6], [25, 5], [25, 4], [25, 3], [25, 2], [25, 1], [25, 0]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,mines = [[25, 25], [25, 24], [25, 23], [25, 22], [25, 21], [25, 20], [25, 19], [25, 18], [25, 17], [25, 16], [25, 15], [25, 14], [25, 13], [25, 12], [25, 11], [25, 10], [25, 9], [25, 8], [25, 7], [25, 6], [25, 5], [25, 4], [25, 3], [25, 2], [25, 1], [25, 0]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,mines = [[49, 49], [50, 49], [51, 49], [49, 50], [50, 50], [51, 50], [49, 51], [50, 51], [51, 51], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,mines = [[49, 49], [50, 49], [51, 49], [49, 50], [50, 50], [51, 50], [49, 51], [50, 51], [51, 51], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[10, 10], [10, 11], [10, 12], [10, 9], [9, 10], [9, 11], [9, 12], [9, 9], [11, 10], [11, 11], [11, 12], [11, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[10, 10], [10, 11], [10, 12], [10, 9], [9, 10], [9, 11], [9, 12], [9, 9], [11, 10], [11, 11], [11, 12], [11, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,mines = [[15, 14], [15, 15], [15, 16], [14, 14], [14, 15], [14, 16], [16, 14], [16, 15], [16, 16], [15, 0], [15, 1], [15, 29], [14, 0], [14, 1], [14, 29], [16, 0], [16, 1], [16, 29], [0, 15], [1, 15], [29, 15], [0, 14], [0, 16], [29, 14], [29, 16]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,mines = [[15, 14], [15, 15], [15, 16], [14, 14], [14, 15], [14, 16], [16, 14], [16, 15], [16, 16], [15, 0], [15, 1], [15, 29], [14, 0], [14, 1], [14, 29], [16, 0], [16, 1], [16, 29], [0, 15], [1, 15], [29, 15], [0, 14], [0, 16], [29, 14], [29, 16]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,mines = [[25, 24], [25, 25], [25, 26], [24, 24], [24, 25], [24, 26], [26, 24], [26, 25], [26, 26], [10, 10], [10, 11], [10, 12], [9, 10], [9, 11], [9, 12], [11, 10], [11, 11], [11, 12]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,mines = [[25, 24], [25, 25], [25, 26], [24, 24], [24, 25], [24, 26], [26, 24], [26, 25], [26, 26], [10, 10], [10, 11], [10, 12], [9, 10], [9, 11], [9, 12], [11, 10], [11, 11], [11, 12]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[9, 9], [9, 10], [10, 9], [8, 9], [9, 8], [9, 11], [11, 9], [7, 9], [9, 7], [10, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[9, 9], [9, 10], [10, 9], [8, 9], [9, 8], [9, 11], [11, 9], [7, 9], [9, 7], [10, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,mines = [[3, 3], [4, 4], [5, 5], [3, 4], [4, 3], [3, 5], [4, 5], [5, 3], [5, 4], [5, 6], [6, 5], [6, 3], [6, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,mines = [[3, 3], [4, 4], [5, 5], [3, 4], [4, 3], [3, 5], [4, 5], [5, 3], [5, 4], [5, 6], [6, 5], [6, 3], [6, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,mines = [[150, 150], [151, 151], [149, 149], [152, 152], [148, 148]]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,mines = [[150, 150], [151, 151], [149, 149], [152, 152], [148, 148]]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,mines = [[0, 0], [0, 1], [0, 2], [0, 27], [0, 28], [0, 29], [1, 0], [1, 29], [2, 0], [2, 29], [27, 0], [27, 29], [28, 0], [28, 29], [29, 0], [29, 1], [29, 2], [29, 27], [29, 28], [29, 29], [10, 10], [10, 19], [19, 10], [19, 19]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,mines = [[0, 0], [0, 1], [0, 2], [0, 27], [0, 28], [0, 29], [1, 0], [1, 29], [2, 0], [2, 29], [27, 0], [27, 29], [28, 0], [28, 29], [29, 0], [29, 1], [29, 2], [29, 27], [29, 28], [29, 29], [10, 10], [10, 19], [19, 10], [19, 19]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [6, 7], [7, 6], [7, 9], [9, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [6, 7], [7, 6], [7, 9], [9, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[5, 5], [4, 5], [6, 5], [5, 4], [5, 6], [0, 0], [9, 9], [0, 9], [9, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[5, 5], [4, 5], [6, 5], [5, 4], [5, 6], [0, 0], [9, 9], [0, 9], [9, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,mines = [[10, 10], [9, 10], [11, 10], [10, 9], [10, 11], [5, 5], [15, 15], [0, 0], [19, 19], [1, 1], [18, 18]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,mines = [[10, 10], [9, 10], [11, 10], [10, 9], [10, 11], [5, 5], [15, 15], [0, 0], [19, 19], [1, 1], [18, 18]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [7, 6], [6, 8], [8, 6], [8, 9], [9, 8], [7, 9], [9, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [7, 6], [6, 8], [8, 6], [8, 9], [9, 8], [7, 9], [9, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [11, 11]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [11, 11]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [251, 250], [249, 250], [250, 251], [250, 249]]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [251, 250], [249, 250], [250, 251], [250, 249]]) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,mines = [[25, 25], [24, 24], [24, 26], [26, 24], [26, 26], [10, 10], [10, 39], [39, 10], [39, 39]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,mines = [[25, 25], [24, 24], [24, 26], [26, 24], [26, 26], [10, 10], [10, 39], [39, 10], [39, 39]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253], [246, 246], [254, 254], [245, 245], [255, 255]]) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253], [246, 246], [254, 254], [245, 245], [255, 255]]) == 245: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 9], [2, 0], [2, 9], [3, 0], [3, 9], [4, 0], [4, 9], [5, 0], [5, 9], [6, 0], [6, 9], [7, 0], [7, 9], [8, 0], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 9], [2, 0], [2, 9], [3, 0], [3, 9], [4, 0], [4, 9], [5, 0], [5, 9], [6, 0], [6, 9], [7, 0], [7, 9], [8, 0], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,mines = [[250, 250], [250, 251], [251, 250], [251, 251]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,mines = [[250, 250], [250, 251], [251, 250], [251, 251]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 4], [4, 2], [5, 3], [3, 5], [5, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 4], [4, 2], [5, 3], [3, 5], [5, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12], [15, 15], [15, 16], [15, 17], [16, 15], [16, 16], [16, 17], [17, 15], [17, 16], [17, 17]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12], [15, 15], [15, 16], [15, 17], [16, 15], [16, 16], [16, 17], [17, 15], [17, 16], [17, 17]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,mines = [[4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [4, 6], [4, 7], [4, 8], [4, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,mines = [[4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [4, 6], [4, 7], [4, 8], [4, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 8], [8, 9], [9, 7], [9, 8], [9, 9], [6, 6], [6, 10], [10, 6], [10, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 8], [8, 9], [9, 7], [9, 8], [9, 9], [6, 6], [6, 10], [10, 6], [10, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,mines = [[200, 200], [199, 199], [199, 201], [201, 199], [201, 201], [199, 200], [200, 199], [200, 201], [150, 150], [250, 250]]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,mines = [[200, 200], [199, 199], [199, 201], [201, 199], [201, 201], [199, 200], [200, 199], [200, 201], [150, 150], [250, 250]]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [3, 2], [4, 2], [5, 2], [3, 6], [4, 6], [5, 6], [2, 3], [2, 4], [2, 5], [6, 3], [6, 4], [6, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [3, 2], [4, 2], [5, 2], [3, 6], [4, 6], [5, 6], [2, 3], [2, 4], [2, 5], [6, 3], [6, 4], [6, 5]]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 6], [2, 0], [2, 6], [3, 0], [3, 6], [4, 0], [4, 6], [5, 0], [5, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]) == 3
    assert candidate(n = 4,mines = [[0, 0], [0, 3], [3, 0], [3, 3]]) == 2
    assert candidate(n = 5,mines = [[1, 1], [1, 3], [3, 1], [3, 3]]) == 3
    assert candidate(n = 5,mines = [[0, 0], [0, 4], [4, 0], [4, 4]]) == 3
    assert candidate(n = 6,mines = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 2
    assert candidate(n = 6,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]]) == 2
    assert candidate(n = 1,mines = [[0, 0]]) == 0
    assert candidate(n = 500,mines = [[250, 250]]) == 250
    assert candidate(n = 4,mines = [[0, 0], [3, 3]]) == 2
    assert candidate(n = 3,mines = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]) == 1
    assert candidate(n = 3,mines = [[1, 1]]) == 1
    assert candidate(n = 5,mines = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]]) == 1
    assert candidate(n = 500,mines = []) == 250
    assert candidate(n = 4,mines = []) == 2
    assert candidate(n = 5,mines = [[4, 2]]) == 2
    assert candidate(n = 3,mines = [[0, 0], [1, 1], [2, 2]]) == 1
    assert candidate(n = 3,mines = []) == 2
    assert candidate(n = 6,mines = [[1, 2], [2, 1], [2, 3], [3, 2]]) == 2
    assert candidate(n = 100,mines = [[50, 50], [49, 49], [49, 51], [51, 49], [51, 51], [49, 50], [50, 49], [50, 51], [60, 60], [30, 30]]) == 49
    assert candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [14, 14]]) == 7
    assert candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253]]) == 247
    assert candidate(n = 25,mines = [[10, 10], [11, 11], [12, 12], [13, 13], [10, 12], [12, 10], [11, 9], [11, 13], [9, 11], [13, 11]]) == 11
    assert candidate(n = 10,mines = [[0, 0], [9, 9], [0, 9], [9, 0], [4, 4], [5, 5]]) == 4
    assert candidate(n = 10,mines = [[5, 5], [5, 6], [6, 5], [4, 5], [5, 4]]) == 4
    assert candidate(n = 15,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]]) == 7
    assert candidate(n = 75,mines = [[37, 37], [36, 36], [36, 38], [38, 36], [38, 38], [36, 37], [37, 36], [37, 38]]) == 36
    assert candidate(n = 30,mines = [[10, 10], [11, 10], [9, 10], [10, 9], [10, 11], [15, 15], [14, 15], [16, 15], [15, 14], [15, 16], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 14
    assert candidate(n = 20,mines = [[5, 5], [5, 14], [14, 5], [14, 14], [10, 10], [10, 9], [9, 10], [9, 9], [10, 8], [8, 10], [0, 0], [19, 19]]) == 9
    assert candidate(n = 500,mines = [[250, 250], [249, 249], [249, 251], [251, 249], [251, 251], [249, 250], [250, 249], [250, 251], [200, 200], [300, 300]]) == 249
    assert candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0]]) == 2
    assert candidate(n = 100,mines = [[50, 50], [49, 49], [51, 51], [48, 48], [52, 52], [47, 47], [53, 53], [46, 46], [54, 54], [45, 45], [55, 55]]) == 45
    assert candidate(n = 500,mines = [[250, 250], [250, 251], [250, 249], [249, 250], [251, 250]]) == 249
    assert candidate(n = 10,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 3
    assert candidate(n = 12,mines = [[0, 0], [11, 11], [5, 5], [6, 5], [5, 6], [6, 6], [7, 7], [8, 8], [4, 4], [4, 3], [4, 2], [3, 4], [2, 4]]) == 4
    assert candidate(n = 20,mines = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]]) == 10
    assert candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6]]) == 2
    assert candidate(n = 6,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]) == 1
    assert candidate(n = 25,mines = [[0, 0], [0, 1], [0, 2], [0, 22], [0, 23], [0, 24], [1, 0], [1, 24], [2, 0], [2, 24], [22, 0], [22, 24], [23, 0], [23, 24], [24, 0], [24, 1], [24, 2], [24, 22], [24, 23], [24, 24]]) == 13
    assert candidate(n = 20,mines = [[1, 1], [1, 18], [18, 1], [18, 18], [9, 9], [10, 10], [11, 11]]) == 9
    assert candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 4], [4, 5], [5, 6], [6, 5]]) == 4
    assert candidate(n = 100,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 12], [12, 10], [12, 11], [12, 12]]) == 50
    assert candidate(n = 200,mines = [[100, 100], [100, 101], [101, 100], [99, 99], [101, 99], [99, 101], [98, 98], [102, 102]]) == 98
    assert candidate(n = 10,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 3
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 9], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 5
    assert candidate(n = 15,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]]) == 8
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [7, 9], [8, 9], [9, 7], [9, 8], [9, 9]]) == 7
    assert candidate(n = 10,mines = [[0, 5], [5, 0], [5, 5], [9, 5], [5, 9]]) == 5
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [6, 8], [6, 9], [7, 6], [7, 9], [8, 6], [8, 9], [9, 6], [9, 7], [9, 8], [9, 9], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 10], [7, 5], [7, 10], [8, 5], [8, 10], [9, 5], [9, 10], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == 5
    assert candidate(n = 25,mines = [[12, 12], [11, 11], [13, 13], [10, 10], [11, 10], [10, 11], [13, 12], [12, 11], [11, 13], [12, 13], [13, 11], [10, 12], [12, 10], [12, 14], [14, 12], [11, 12], [13, 12], [12, 11], [12, 13]]) == 10
    assert candidate(n = 10,mines = [[5, 5], [4, 4], [6, 6], [5, 6], [6, 5], [5, 4], [4, 5], [3, 3], [7, 7], [2, 2], [8, 8], [1, 1], [9, 9]]) == 3
    assert candidate(n = 7,mines = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 3
    assert candidate(n = 25,mines = [[5, 5], [5, 19], [19, 5], [19, 19], [12, 12], [13, 13], [12, 13], [13, 12]]) == 12
    assert candidate(n = 7,mines = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3], [2, 4], [2, 5], [4, 2], [5, 2], [6, 2]]) == 2
    assert candidate(n = 8,mines = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == 2
    assert candidate(n = 7,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 2
    assert candidate(n = 10,mines = [[4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 4], [6, 5], [6, 6]]) == 4
    assert candidate(n = 30,mines = [[15, 15], [14, 14], [13, 13], [12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 14
    assert candidate(n = 10,mines = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]]) == 3
    assert candidate(n = 8,mines = [[1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5]]) == 4
    assert candidate(n = 300,mines = [[150, 150], [149, 149], [149, 151], [151, 149], [151, 151], [149, 150], [150, 149], [150, 151], [100, 100], [200, 200]]) == 149
    assert candidate(n = 20,mines = [[10, 10], [10, 11], [11, 10], [11, 11], [9, 9], [9, 10], [9, 11], [10, 9], [11, 9], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [9, 8], [9, 12], [10, 8], [10, 12], [11, 8], [11, 12], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [8, 7], [8, 13], [9, 7], [9, 13], [10, 7], [10, 13], [11, 7], [11, 13], [12, 7], [12, 13], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13]]) == 7
    assert candidate(n = 20,mines = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1], [10, 0]]) == 9
    assert candidate(n = 50,mines = [[25, 25], [25, 24], [25, 23], [25, 22], [25, 21], [25, 20], [25, 19], [25, 18], [25, 17], [25, 16], [25, 15], [25, 14], [25, 13], [25, 12], [25, 11], [25, 10], [25, 9], [25, 8], [25, 7], [25, 6], [25, 5], [25, 4], [25, 3], [25, 2], [25, 1], [25, 0]]) == 24
    assert candidate(n = 100,mines = [[49, 49], [50, 49], [51, 49], [49, 50], [50, 50], [51, 50], [49, 51], [50, 51], [51, 51], [20, 20], [21, 20], [19, 20], [20, 19], [20, 21]]) == 49
    assert candidate(n = 20,mines = [[10, 10], [10, 11], [10, 12], [10, 9], [9, 10], [9, 11], [9, 12], [9, 9], [11, 10], [11, 11], [11, 12], [11, 9]]) == 9
    assert candidate(n = 30,mines = [[15, 14], [15, 15], [15, 16], [14, 14], [14, 15], [14, 16], [16, 14], [16, 15], [16, 16], [15, 0], [15, 1], [15, 29], [14, 0], [14, 1], [14, 29], [16, 0], [16, 1], [16, 29], [0, 15], [1, 15], [29, 15], [0, 14], [0, 16], [29, 14], [29, 16]]) == 14
    assert candidate(n = 50,mines = [[25, 24], [25, 25], [25, 26], [24, 24], [24, 25], [24, 26], [26, 24], [26, 25], [26, 26], [10, 10], [10, 11], [10, 12], [9, 10], [9, 11], [9, 12], [11, 10], [11, 11], [11, 12]]) == 24
    assert candidate(n = 20,mines = [[9, 9], [9, 10], [10, 9], [8, 9], [9, 8], [9, 11], [11, 9], [7, 9], [9, 7], [10, 10]]) == 8
    assert candidate(n = 8,mines = [[3, 3], [4, 4], [5, 5], [3, 4], [4, 3], [3, 5], [4, 5], [5, 3], [5, 4], [5, 6], [6, 5], [6, 3], [6, 4]]) == 3
    assert candidate(n = 300,mines = [[150, 150], [151, 151], [149, 149], [152, 152], [148, 148]]) == 148
    assert candidate(n = 6,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 3
    assert candidate(n = 30,mines = [[0, 0], [0, 1], [0, 2], [0, 27], [0, 28], [0, 29], [1, 0], [1, 29], [2, 0], [2, 29], [27, 0], [27, 29], [28, 0], [28, 29], [29, 0], [29, 1], [29, 2], [29, 27], [29, 28], [29, 29], [10, 10], [10, 19], [19, 10], [19, 19]]) == 15
    assert candidate(n = 10,mines = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 5
    assert candidate(n = 25,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 10
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [6, 7], [7, 6], [7, 9], [9, 7]]) == 6
    assert candidate(n = 10,mines = [[5, 5], [4, 5], [6, 5], [5, 4], [5, 6], [0, 0], [9, 9], [0, 9], [9, 0]]) == 4
    assert candidate(n = 20,mines = [[10, 10], [9, 10], [11, 10], [10, 9], [10, 11], [5, 5], [15, 15], [0, 0], [19, 19], [1, 1], [18, 18]]) == 9
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [8, 7], [8, 8], [6, 6], [6, 7], [7, 6], [6, 8], [8, 6], [8, 9], [9, 8], [7, 9], [9, 7]]) == 6
    assert candidate(n = 12,mines = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [0, 0], [11, 11]]) == 5
    assert candidate(n = 500,mines = [[250, 250], [251, 250], [249, 250], [250, 251], [250, 249]]) == 249
    assert candidate(n = 50,mines = [[25, 25], [24, 24], [24, 26], [26, 24], [26, 26], [10, 10], [10, 39], [39, 10], [39, 39]]) == 24
    assert candidate(n = 500,mines = [[250, 250], [249, 249], [251, 251], [248, 248], [252, 252], [247, 247], [253, 253], [246, 246], [254, 254], [245, 245], [255, 255]]) == 245
    assert candidate(n = 10,mines = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 9], [2, 0], [2, 9], [3, 0], [3, 9], [4, 0], [4, 9], [5, 0], [5, 9], [6, 0], [6, 9], [7, 0], [7, 9], [8, 0], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == 4
    assert candidate(n = 500,mines = [[250, 250], [250, 251], [251, 250], [251, 251]]) == 250
    assert candidate(n = 7,mines = [[3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 4], [4, 2], [5, 3], [3, 5], [5, 5]]) == 2
    assert candidate(n = 30,mines = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12], [15, 15], [15, 16], [15, 17], [16, 15], [16, 16], [16, 17], [17, 15], [17, 16], [17, 17]]) == 15
    assert candidate(n = 12,mines = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 4
    assert candidate(n = 10,mines = [[4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [4, 6], [4, 7], [4, 8], [4, 9]]) == 3
    assert candidate(n = 15,mines = [[7, 7], [7, 8], [7, 9], [8, 7], [8, 8], [8, 9], [9, 7], [9, 8], [9, 9], [6, 6], [6, 10], [10, 6], [10, 10]]) == 6
    assert candidate(n = 400,mines = [[200, 200], [199, 199], [199, 201], [201, 199], [201, 201], [199, 200], [200, 199], [200, 201], [150, 150], [250, 250]]) == 199
    assert candidate(n = 8,mines = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [3, 2], [4, 2], [5, 2], [3, 6], [4, 6], [5, 6], [2, 3], [2, 4], [2, 5], [6, 3], [6, 4], [6, 5]]) == 2


