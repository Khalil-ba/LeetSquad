def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,time = [[2, 10, 1, 5], [3, 1, 2, 2], [1, 5, 0, 1], [4, 3, 2, 1]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,time = [[2, 10, 1, 5], [3, 1, 2, 2], [1, 5, 0, 1], [4, 3, 2, 1]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1,time = [[1, 2, 3, 4]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1,time = [[1, 2, 3, 4]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1,time = [[1, 2, 1, 2]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1,time = [[1, 2, 1, 2]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1,time = [[5, 5, 5, 5]]) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1,time = [[5, 5, 5, 5]]) == 195: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,time = [[1, 2, 1, 2], [3, 4, 3, 4], [2, 3, 2, 3]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,time = [[1, 2, 1, 2], [3, 4, 3, 4], [2, 3, 2, 3]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 4,time = [[2, 10, 1, 1], [3, 1, 2, 2], [1, 4, 3, 3], [1, 1, 5, 5]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 4,time = [[2, 10, 1, 1], [3, 1, 2, 2], [1, 4, 3, 3], [1, 1, 5, 5]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,time = [[2, 1, 3, 2], [4, 3, 5, 4], [3, 2, 4, 3], [1, 1, 2, 1], [2, 2, 3, 3]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,time = [[2, 1, 3, 2], [4, 3, 5, 4], [3, 2, 4, 3], [1, 1, 2, 1], [2, 2, 3, 3]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2,time = [[1, 1, 2, 2], [3, 3, 4, 4]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2,time = [[1, 1, 2, 2], [3, 3, 4, 4]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,time = [[1, 5, 1, 8], [10, 10, 10, 10]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,time = [[1, 5, 1, 8], [10, 10, 10, 10]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 3,time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 3,time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,time = [[1, 2, 1, 2], [2, 2, 2, 2], [3, 2, 3, 3], [4, 2, 4, 4]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,time = [[1, 2, 1, 2], [2, 2, 2, 2], [3, 2, 3, 3], [4, 2, 4, 4]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,time = [[2, 3, 2, 2], [4, 4, 3, 3], [1, 2, 1, 1], [5, 5, 5, 5], [3, 3, 3, 3]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,time = [[2, 3, 2, 2], [4, 4, 3, 3], [1, 2, 1, 1], [5, 5, 5, 5], [3, 3, 3, 3]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10,time = [[5, 1, 5, 1], [4, 2, 4, 2], [3, 3, 3, 3], [2, 4, 2, 4], [1, 5, 1, 5], [2, 3, 2, 3], [3, 2, 3, 2], [4, 1, 4, 1], [5, 4, 5, 4], [6, 5, 6, 5]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10,time = [[5, 1, 5, 1], [4, 2, 4, 2], [3, 3, 3, 3], [2, 4, 2, 4], [1, 5, 1, 5], [2, 3, 2, 3], [3, 2, 3, 2], [4, 1, 4, 1], [5, 4, 5, 4], [6, 5, 6, 5]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 7,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2], [5, 5, 5, 5], [2, 2, 2, 2]]) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 7,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2], [5, 5, 5, 5], [2, 2, 2, 2]]) == 143: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 163: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 4,time = [[10, 5, 15, 20], [5, 10, 10, 15], [20, 25, 30, 5], [15, 15, 10, 10]]) == 875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 4,time = [[10, 5, 15, 20], [5, 10, 10, 15], [20, 25, 30, 5], [15, 15, 10, 10]]) == 875: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,time = [[1, 1, 1, 10], [2, 2, 2, 20], [3, 3, 3, 30], [4, 4, 4, 40], [5, 5, 5, 50]]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,time = [[1, 1, 1, 10], [2, 2, 2, 20], [3, 3, 3, 30], [4, 4, 4, 40], [5, 5, 5, 50]]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 4,time = [[10, 10, 1, 1], [5, 5, 2, 2], [3, 3, 3, 3], [1, 1, 5, 5]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 4,time = [[10, 10, 1, 1], [5, 5, 2, 2], [3, 3, 3, 3], [1, 1, 5, 5]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 3,time = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 3,time = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 3,time = [[3, 2, 2, 1], [4, 3, 3, 2], [5, 4, 4, 3]]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 3,time = [[3, 2, 2, 1], [4, 3, 3, 2], [5, 4, 4, 3]]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 3,time = [[1, 10, 1, 1], [2, 9, 2, 2], [3, 8, 3, 3]]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 3,time = [[1, 10, 1, 1], [2, 9, 2, 2], [3, 8, 3, 3]]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,time = [[2, 1, 3, 2], [1, 2, 4, 1], [3, 1, 1, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,time = [[2, 1, 3, 2], [1, 2, 4, 1], [3, 1, 1, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 4,time = [[2, 5, 3, 2], [3, 5, 5, 2], [4, 5, 6, 2], [5, 5, 7, 2]]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 4,time = [[2, 5, 3, 2], [3, 5, 5, 2], [4, 5, 6, 2], [5, 5, 7, 2]]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3,time = [[10, 10, 1, 1], [1, 10, 5, 10], [5, 5, 2, 2]]) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3,time = [[10, 10, 1, 1], [1, 10, 5, 10], [5, 5, 2, 2]]) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 309: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 6,time = [[5, 1, 5, 1], [3, 2, 3, 2], [2, 3, 2, 3], [1, 4, 1, 4], [4, 1, 4, 1], [6, 1, 6, 1]]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 6,time = [[5, 1, 5, 1], [3, 2, 3, 2], [2, 3, 2, 3], [1, 4, 1, 4], [4, 1, 4, 1], [6, 1, 6, 1]]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5,time = [[1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1], [1, 1, 1, 1]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5,time = [[1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1], [1, 1, 1, 1]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3,time = [[2, 3, 1, 2], [1, 2, 2, 3], [3, 2, 2, 1]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3,time = [[2, 3, 1, 2], [1, 2, 2, 3], [3, 2, 2, 1]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 10,time = [[1, 2, 1, 2], [2, 1, 2, 1], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 10,time = [[1, 2, 1, 2], [2, 1, 2, 1], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 363: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,time = [[3, 7, 2, 5], [5, 4, 2, 6], [1, 3, 1, 2], [4, 6, 3, 8], [2, 2, 2, 2]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,time = [[3, 7, 2, 5], [5, 4, 2, 6], [1, 3, 1, 2], [4, 6, 3, 8], [2, 2, 2, 2]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 4,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 4,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]) == 163: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 3, 3, 1], [1, 4, 4, 1]]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 3, 3, 1], [1, 4, 4, 1]]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 9,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7], [1, 8, 1, 8], [1, 9, 1, 9]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 9,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7], [1, 8, 1, 8], [1, 9, 1, 9]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 5,time = [[1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5], [5, 5, 6, 6]]) == 367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 5,time = [[1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5], [5, 5, 6, 6]]) == 367: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 6,time = [[2, 3, 2, 3], [3, 2, 3, 2], [1, 4, 1, 4], [4, 1, 4, 1], [5, 5, 5, 5], [6, 6, 6, 6]]) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 6,time = [[2, 3, 2, 3], [3, 2, 3, 2], [1, 4, 1, 4], [4, 1, 4, 1], [5, 5, 5, 5], [6, 6, 6, 6]]) == 258: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8,time = [[1, 2, 3, 4], [8, 7, 6, 5], [1, 3, 5, 7], [2, 4, 6, 8], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8,time = [[1, 2, 3, 4], [8, 7, 6, 5], [1, 3, 5, 7], [2, 4, 6, 8], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 1812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 1812: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 5,time = [[5, 10, 5, 10], [10, 5, 10, 5], [5, 10, 10, 5], [10, 5, 5, 10], [5, 5, 5, 5]]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 5,time = [[5, 10, 5, 10], [10, 5, 10, 5], [5, 10, 10, 5], [10, 5, 5, 10], [5, 5, 5, 5]]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 3,time = [[3, 1, 2, 1], [2, 2, 3, 2], [1, 3, 1, 3]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 3,time = [[3, 1, 2, 1], [2, 2, 3, 2], [1, 3, 1, 3]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,time = [[1, 1, 1, 100], [2, 2, 2, 90], [3, 3, 3, 80]]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,time = [[1, 1, 1, 100], [2, 2, 2, 90], [3, 3, 3, 80]]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 403: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 8,time = [[1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3], [4, 4, 4, 4], [4, 4, 4, 4]]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 8,time = [[1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3], [4, 4, 4, 4], [4, 4, 4, 4]]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 7,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7]]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 7,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7]]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 3,time = [[10, 10, 10, 10], [15, 15, 15, 15], [5, 5, 5, 5]]) == 415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 3,time = [[10, 10, 10, 10], [15, 15, 15, 15], [5, 5, 5, 5]]) == 415: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 2, 1, 2], [2, 1, 2, 1], [1, 3, 1, 3], [2, 2, 2, 2], [1, 4, 1, 4], [2, 3, 2, 3], [3, 2, 3, 2], [3, 3, 3, 3], [4, 1, 4, 1]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 2, 1, 2], [2, 1, 2, 1], [1, 3, 1, 3], [2, 2, 2, 2], [1, 4, 1, 4], [2, 3, 2, 3], [3, 2, 3, 2], [3, 3, 3, 3], [4, 1, 4, 1]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 6,time = [[5, 2, 3, 1], [2, 3, 4, 2], [1, 4, 5, 3], [3, 5, 1, 4], [2, 1, 4, 5], [4, 3, 2, 6]]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 6,time = [[5, 2, 3, 1], [2, 3, 4, 2], [1, 4, 5, 3], [3, 5, 1, 4], [2, 1, 4, 5], [4, 3, 2, 6]]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 7,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 7,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5,time = [[2, 3, 2, 1], [1, 1, 1, 1], [3, 2, 3, 2], [2, 2, 2, 2], [1, 3, 1, 3]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5,time = [[2, 3, 2, 1], [1, 1, 1, 1], [3, 2, 3, 2], [2, 2, 2, 2], [1, 3, 1, 3]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 5,time = [[1, 1, 10, 10], [2, 2, 9, 9], [3, 3, 8, 8], [4, 4, 7, 7], [5, 5, 6, 6]]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 5,time = [[1, 1, 10, 10], [2, 2, 9, 9], [3, 3, 8, 8], [4, 4, 7, 7], [5, 5, 6, 6]]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 7,time = [[5, 3, 4, 2], [2, 1, 2, 1], [3, 2, 3, 2], [1, 5, 1, 5], [4, 4, 4, 4], [6, 6, 6, 6], [7, 7, 7, 7]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 7,time = [[5, 3, 4, 2], [2, 1, 2, 1], [3, 2, 3, 2], [1, 5, 1, 5], [4, 4, 4, 4], [6, 6, 6, 6], [7, 7, 7, 7]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 8,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 1410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 8,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 1410: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 4,time = [[10, 10, 1, 1], [1, 1, 10, 10], [5, 5, 5, 5], [2, 2, 2, 2]]) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 4,time = [[10, 10, 1, 1], [1, 1, 10, 10], [5, 5, 5, 5], [2, 2, 2, 2]]) == 209: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,k = 12,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12]]) == 1320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,k = 12,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12]]) == 1320: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 8,time = [[2, 1, 3, 4], [4, 2, 1, 3], [1, 2, 2, 1], [3, 3, 3, 3], [5, 4, 4, 5], [2, 2, 2, 2], [3, 1, 2, 1], [4, 3, 1, 4]]) == 268
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 8,time = [[2, 1, 3, 4], [4, 2, 1, 3], [1, 2, 2, 1], [3, 3, 3, 3], [5, 4, 4, 5], [2, 2, 2, 2], [3, 1, 2, 1], [4, 3, 1, 4]]) == 268: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 6,time = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 9, 8, 7], [8, 7, 6, 5], [5, 4, 3, 2]]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 6,time = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 9, 8, 7], [8, 7, 6, 5], [5, 4, 3, 2]]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3,time = [[5, 2, 3, 2], [3, 5, 3, 2], [2, 3, 4, 2]]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3,time = [[5, 2, 3, 2], [3, 5, 3, 2], [2, 3, 4, 2]]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 6,time = [[2, 5, 3, 7], [3, 4, 2, 6], [4, 3, 5, 2], [1, 6, 4, 3], [5, 2, 1, 4], [6, 1, 3, 5]]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 6,time = [[2, 5, 3, 7], [3, 4, 2, 6], [4, 3, 5, 2], [1, 6, 4, 3], [5, 2, 1, 4], [6, 1, 3, 5]]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3,time = [[2, 3, 4, 5], [1, 4, 3, 2], [3, 2, 5, 1]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3,time = [[2, 3, 4, 5], [1, 4, 3, 2], [3, 2, 5, 1]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 4,time = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 1, 1, 3]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 4,time = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 1, 1, 3]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 4,time = [[2, 1, 2, 1], [4, 2, 4, 2], [3, 3, 3, 3], [5, 5, 5, 5]]) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 4,time = [[2, 1, 2, 1], [4, 2, 4, 2], [3, 3, 3, 3], [5, 5, 5, 5]]) == 207: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 3,time = [[10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1]]) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 3,time = [[10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1]]) == 276: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5,time = [[2, 2, 2, 2], [3, 3, 3, 3], [1, 1, 1, 1], [4, 4, 4, 4], [5, 5, 5, 5]]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5,time = [[2, 2, 2, 2], [3, 3, 3, 3], [1, 1, 1, 1], [4, 4, 4, 4], [5, 5, 5, 5]]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3,time = [[5, 1, 2, 1], [2, 1, 5, 2], [1, 1, 1, 1]]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3,time = [[5, 1, 2, 1], [2, 1, 5, 2], [1, 1, 1, 1]]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 5,time = [[2, 3, 4, 1], [1, 2, 3, 1], [5, 3, 2, 1], [4, 1, 3, 2], [3, 2, 1, 5]]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 5,time = [[2, 3, 4, 1], [1, 2, 3, 1], [5, 3, 2, 1], [4, 1, 3, 2], [3, 2, 1, 5]]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 6,time = [[2, 3, 2, 3], [1, 1, 1, 1], [5, 5, 5, 5], [3, 2, 3, 2], [2, 5, 2, 5], [4, 4, 4, 4]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 6,time = [[2, 3, 2, 3], [1, 1, 1, 1], [5, 5, 5, 5], [3, 2, 3, 2], [2, 5, 2, 5], [4, 4, 4, 4]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 6,time = [[1, 5, 1, 8], [10, 10, 10, 10], [3, 2, 1, 4], [2, 1, 2, 3], [1, 4, 3, 2], [4, 3, 2, 1]]) == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 6,time = [[1, 5, 1, 8], [10, 10, 10, 10], [3, 2, 1, 4], [2, 1, 2, 3], [1, 4, 3, 2], [4, 3, 2, 1]]) == 178: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 6,time = [[3, 2, 2, 1], [2, 1, 3, 2], [4, 3, 3, 4], [1, 2, 1, 2], [5, 5, 5, 5], [0, 0, 0, 0]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 6,time = [[3, 2, 2, 1], [2, 1, 3, 2], [4, 3, 3, 4], [1, 2, 1, 2], [5, 5, 5, 5], [0, 0, 0, 0]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 6,time = [[1, 1, 1, 10], [1, 1, 1, 9], [1, 1, 1, 8], [1, 1, 1, 7], [1, 1, 1, 6], [1, 1, 1, 5]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 6,time = [[1, 1, 1, 10], [1, 1, 1, 9], [1, 1, 1, 8], [1, 1, 1, 7], [1, 1, 1, 6], [1, 1, 1, 5]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 1812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 1812: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 4,time = [[1, 4, 2, 3], [3, 2, 1, 4], [2, 3, 4, 1], [4, 1, 3, 2]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 4,time = [[1, 4, 2, 3], [3, 2, 1, 4], [2, 3, 4, 1], [4, 1, 3, 2]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 3,time = [[3, 3, 2, 2], [2, 2, 3, 3], [1, 1, 1, 1]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 3,time = [[3, 3, 2, 2], [2, 2, 3, 3], [1, 1, 1, 1]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3,time = [[10, 5, 10, 5], [5, 10, 5, 10], [1, 1, 1, 1]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3,time = [[10, 5, 10, 5], [5, 10, 5, 10], [1, 1, 1, 1]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 4,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1], [3, 4, 1, 2]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 4,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1], [3, 4, 1, 2]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 4,time = [[5, 1, 1, 5], [1, 5, 5, 1], [3, 3, 3, 3], [2, 2, 2, 2]]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 4,time = [[5, 1, 1, 5], [1, 5, 5, 1], [3, 3, 3, 3], [2, 2, 2, 2]]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 4,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7]]) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 4,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7]]) == 462: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2], [3, 1, 4, 1], [5, 5, 5, 5]]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2], [3, 1, 4, 1], [5, 5, 5, 5]]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 5,time = [[1, 1, 10, 1], [1, 1, 9, 1], [1, 1, 8, 1], [1, 1, 7, 1], [1, 1, 6, 1]]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 5,time = [[1, 1, 10, 1], [1, 1, 9, 1], [1, 1, 8, 1], [1, 1, 7, 1], [1, 1, 6, 1]]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 6,time = [[3, 2, 1, 2], [2, 2, 2, 2], [1, 2, 3, 2], [4, 2, 4, 2], [5, 2, 5, 2], [6, 2, 6, 2]]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 6,time = [[3, 2, 1, 2], [2, 2, 2, 2], [1, 2, 3, 2], [4, 2, 4, 2], [5, 2, 5, 2], [6, 2, 6, 2]]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 6,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4], [4, 5, 4, 5], [5, 6, 5, 6], [6, 7, 6, 7]]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 6,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4], [4, 5, 4, 5], [5, 6, 5, 6], [6, 7, 6, 7]]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 903: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5,time = [[2, 3, 4, 5], [1, 2, 3, 4], [3, 1, 2, 1], [4, 4, 1, 3], [5, 5, 5, 5]]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5,time = [[2, 3, 4, 5], [1, 2, 3, 4], [3, 1, 2, 1], [4, 4, 1, 3], [5, 5, 5, 5]]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5,time = [[5, 2, 3, 2], [4, 3, 2, 5], [3, 5, 1, 3], [2, 4, 1, 4], [1, 6, 2, 6]]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5,time = [[5, 2, 3, 2], [4, 3, 2, 5], [3, 5, 1, 3], [2, 4, 1, 4], [1, 6, 2, 6]]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4]]) == 52: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,k = 4,time = [[2, 10, 1, 5], [3, 1, 2, 2], [1, 5, 0, 1], [4, 3, 2, 1]]) == 31
    assert candidate(n = 2,k = 1,time = [[1, 2, 3, 4]]) == 16
    assert candidate(n = 5,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 54
    assert candidate(n = 7,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 48
    assert candidate(n = 5,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 43
    assert candidate(n = 2,k = 1,time = [[1, 2, 1, 2]]) == 10
    assert candidate(n = 10,k = 1,time = [[5, 5, 5, 5]]) == 195
    assert candidate(n = 5,k = 3,time = [[1, 2, 1, 2], [3, 4, 3, 4], [2, 3, 2, 3]]) == 26
    assert candidate(n = 10,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 45
    assert candidate(n = 6,k = 3,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 24
    assert candidate(n = 2,k = 4,time = [[2, 10, 1, 1], [3, 1, 2, 2], [1, 4, 3, 3], [1, 1, 5, 5]]) == 11
    assert candidate(n = 10,k = 5,time = [[2, 1, 3, 2], [4, 3, 5, 4], [3, 2, 4, 3], [1, 1, 2, 1], [2, 2, 3, 3]]) == 80
    assert candidate(n = 10,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 108
    assert candidate(n = 4,k = 2,time = [[1, 1, 2, 2], [3, 3, 4, 4]]) == 25
    assert candidate(n = 10,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 87
    assert candidate(n = 3,k = 2,time = [[1, 5, 1, 8], [10, 10, 10, 10]]) == 37
    assert candidate(n = 1,k = 3,time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]) == 6
    assert candidate(n = 5,k = 4,time = [[1, 2, 1, 2], [2, 2, 2, 2], [3, 2, 3, 3], [4, 2, 4, 4]]) == 34
    assert candidate(n = 15,k = 5,time = [[2, 3, 2, 2], [4, 4, 3, 3], [1, 2, 1, 1], [5, 5, 5, 5], [3, 3, 3, 3]]) == 115
    assert candidate(n = 10,k = 10,time = [[5, 1, 5, 1], [4, 2, 4, 2], [3, 3, 3, 3], [2, 4, 2, 4], [1, 5, 1, 5], [2, 3, 2, 3], [3, 2, 3, 2], [4, 1, 4, 1], [5, 4, 5, 4], [6, 5, 6, 5]]) == 110
    assert candidate(n = 20,k = 7,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2], [5, 5, 5, 5], [2, 2, 2, 2]]) == 143
    assert candidate(n = 20,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 163
    assert candidate(n = 25,k = 4,time = [[10, 5, 15, 20], [5, 10, 10, 15], [20, 25, 30, 5], [15, 15, 10, 10]]) == 875
    assert candidate(n = 12,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 120
    assert candidate(n = 10,k = 5,time = [[1, 1, 1, 10], [2, 2, 2, 20], [3, 3, 3, 30], [4, 4, 4, 40], [5, 5, 5, 50]]) == 77
    assert candidate(n = 8,k = 4,time = [[10, 10, 1, 1], [5, 5, 2, 2], [3, 3, 3, 3], [1, 1, 5, 5]]) == 60
    assert candidate(n = 25,k = 3,time = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 255
    assert candidate(n = 20,k = 3,time = [[3, 2, 2, 1], [4, 3, 3, 2], [5, 4, 4, 3]]) == 160
    assert candidate(n = 50,k = 3,time = [[1, 10, 1, 1], [2, 9, 2, 2], [3, 8, 3, 3]]) == 288
    assert candidate(n = 15,k = 5,time = [[2, 1, 3, 2], [1, 2, 4, 1], [3, 1, 1, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 74
    assert candidate(n = 10,k = 4,time = [[2, 5, 3, 2], [3, 5, 5, 2], [4, 5, 6, 2], [5, 5, 7, 2]]) == 107
    assert candidate(n = 15,k = 3,time = [[10, 10, 1, 1], [1, 10, 5, 10], [5, 5, 2, 2]]) == 142
    assert candidate(n = 25,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 309
    assert candidate(n = 30,k = 6,time = [[5, 1, 5, 1], [3, 2, 3, 2], [2, 3, 2, 3], [1, 4, 1, 4], [4, 1, 4, 1], [6, 1, 6, 1]]) == 330
    assert candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2]]) == 80
    assert candidate(n = 50,k = 5,time = [[1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1], [1, 1, 1, 1]]) == 550
    assert candidate(n = 10,k = 3,time = [[2, 3, 1, 2], [1, 2, 2, 3], [3, 2, 2, 1]]) == 40
    assert candidate(n = 20,k = 10,time = [[1, 2, 1, 2], [2, 1, 2, 1], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 363
    assert candidate(n = 15,k = 5,time = [[3, 7, 2, 5], [5, 4, 2, 6], [1, 3, 1, 2], [4, 6, 3, 8], [2, 2, 2, 2]]) == 90
    assert candidate(n = 20,k = 4,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]) == 163
    assert candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 3, 3, 1], [1, 4, 4, 1]]) == 99
    assert candidate(n = 50,k = 9,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7], [1, 8, 1, 8], [1, 9, 1, 9]]) == 115
    assert candidate(n = 40,k = 5,time = [[1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5], [5, 5, 6, 6]]) == 367
    assert candidate(n = 8,k = 8,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 115
    assert candidate(n = 25,k = 6,time = [[2, 3, 2, 3], [3, 2, 3, 2], [1, 4, 1, 4], [4, 1, 4, 1], [5, 5, 5, 5], [6, 6, 6, 6]]) == 258
    assert candidate(n = 8,k = 8,time = [[1, 2, 3, 4], [8, 7, 6, 5], [1, 3, 5, 7], [2, 4, 6, 8], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72
    assert candidate(n = 100,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 1812
    assert candidate(n = 40,k = 5,time = [[5, 10, 5, 10], [10, 5, 10, 5], [5, 10, 10, 5], [10, 5, 5, 10], [5, 5, 5, 5]]) == 700
    assert candidate(n = 15,k = 5,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]) == 150
    assert candidate(n = 12,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 72
    assert candidate(n = 20,k = 3,time = [[3, 1, 2, 1], [2, 2, 3, 2], [1, 3, 1, 3]]) == 100
    assert candidate(n = 5,k = 3,time = [[1, 1, 1, 100], [2, 2, 2, 90], [3, 3, 3, 80]]) == 107
    assert candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3]]) == 180
    assert candidate(n = 30,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 240
    assert candidate(n = 50,k = 5,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == 403
    assert candidate(n = 30,k = 8,time = [[1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3], [4, 4, 4, 4], [4, 4, 4, 4]]) == 240
    assert candidate(n = 30,k = 7,time = [[1, 1, 1, 1], [1, 2, 1, 2], [1, 3, 1, 3], [1, 4, 1, 4], [1, 5, 1, 5], [1, 6, 1, 6], [1, 7, 1, 7]]) == 74
    assert candidate(n = 20,k = 3,time = [[10, 10, 10, 10], [15, 15, 15, 15], [5, 5, 5, 5]]) == 415
    assert candidate(n = 30,k = 10,time = [[1, 1, 1, 1], [1, 2, 1, 2], [2, 1, 2, 1], [1, 3, 1, 3], [2, 2, 2, 2], [1, 4, 1, 4], [2, 3, 2, 3], [3, 2, 3, 2], [3, 3, 3, 3], [4, 1, 4, 1]]) == 210
    assert candidate(n = 12,k = 6,time = [[5, 2, 3, 1], [2, 3, 4, 2], [1, 4, 5, 3], [3, 5, 1, 4], [2, 1, 4, 5], [4, 3, 2, 6]]) == 84
    assert candidate(n = 30,k = 7,time = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]]) == 420
    assert candidate(n = 20,k = 5,time = [[2, 3, 2, 1], [1, 1, 1, 1], [3, 2, 3, 2], [2, 2, 2, 2], [1, 3, 1, 3]]) == 100
    assert candidate(n = 18,k = 5,time = [[1, 1, 10, 10], [2, 2, 9, 9], [3, 3, 8, 8], [4, 4, 7, 7], [5, 5, 6, 6]]) == 198
    assert candidate(n = 18,k = 7,time = [[5, 3, 4, 2], [2, 1, 2, 1], [3, 2, 3, 2], [1, 5, 1, 5], [4, 4, 4, 4], [6, 6, 6, 6], [7, 7, 7, 7]]) == 210
    assert candidate(n = 100,k = 8,time = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]) == 1410
    assert candidate(n = 20,k = 4,time = [[10, 10, 1, 1], [1, 1, 10, 10], [5, 5, 5, 5], [2, 2, 2, 2]]) == 209
    assert candidate(n = 60,k = 12,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12]]) == 1320
    assert candidate(n = 40,k = 8,time = [[2, 1, 3, 4], [4, 2, 1, 3], [1, 2, 2, 1], [3, 3, 3, 3], [5, 4, 4, 5], [2, 2, 2, 2], [3, 1, 2, 1], [4, 3, 1, 4]]) == 268
    assert candidate(n = 10,k = 6,time = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 9, 8, 7], [8, 7, 6, 5], [5, 4, 3, 2]]) == 171
    assert candidate(n = 15,k = 3,time = [[5, 2, 3, 2], [3, 5, 3, 2], [2, 3, 4, 2]]) == 108
    assert candidate(n = 30,k = 6,time = [[2, 5, 3, 7], [3, 4, 2, 6], [4, 3, 5, 2], [1, 6, 4, 3], [5, 2, 1, 4], [6, 1, 3, 5]]) == 270
    assert candidate(n = 25,k = 4,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) == 156
    assert candidate(n = 15,k = 3,time = [[2, 3, 4, 5], [1, 4, 3, 2], [3, 2, 5, 1]]) == 105
    assert candidate(n = 10,k = 4,time = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 1, 1, 3]]) == 25
    assert candidate(n = 25,k = 4,time = [[2, 1, 2, 1], [4, 2, 4, 2], [3, 3, 3, 3], [5, 5, 5, 5]]) == 207
    assert candidate(n = 25,k = 3,time = [[10, 1, 1, 1], [1, 10, 1, 1], [1, 1, 10, 1]]) == 276
    assert candidate(n = 30,k = 5,time = [[2, 2, 2, 2], [3, 3, 3, 3], [1, 1, 1, 1], [4, 4, 4, 4], [5, 5, 5, 5]]) == 240
    assert candidate(n = 15,k = 3,time = [[5, 1, 2, 1], [2, 1, 5, 2], [1, 1, 1, 1]]) == 106
    assert candidate(n = 100,k = 5,time = [[2, 3, 4, 1], [1, 2, 3, 1], [5, 3, 2, 1], [4, 1, 3, 2], [3, 2, 1, 5]]) == 700
    assert candidate(n = 10,k = 6,time = [[2, 3, 2, 3], [1, 1, 1, 1], [5, 5, 5, 5], [3, 2, 3, 2], [2, 5, 2, 5], [4, 4, 4, 4]]) == 87
    assert candidate(n = 25,k = 6,time = [[1, 5, 1, 8], [10, 10, 10, 10], [3, 2, 1, 4], [2, 1, 2, 3], [1, 4, 3, 2], [4, 3, 2, 1]]) == 178
    assert candidate(n = 20,k = 6,time = [[3, 2, 2, 1], [2, 1, 3, 2], [4, 3, 3, 4], [1, 2, 1, 2], [5, 5, 5, 5], [0, 0, 0, 0]]) == 150
    assert candidate(n = 6,k = 6,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]) == 60
    assert candidate(n = 15,k = 6,time = [[1, 1, 1, 10], [1, 1, 1, 9], [1, 1, 1, 8], [1, 1, 1, 7], [1, 1, 1, 6], [1, 1, 1, 5]]) == 31
    assert candidate(n = 100,k = 10,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1]]) == 1812
    assert candidate(n = 8,k = 4,time = [[1, 4, 2, 3], [3, 2, 1, 4], [2, 3, 4, 1], [4, 1, 3, 2]]) == 52
    assert candidate(n = 12,k = 3,time = [[3, 3, 2, 2], [2, 2, 3, 3], [1, 1, 1, 1]]) == 49
    assert candidate(n = 7,k = 3,time = [[10, 5, 10, 5], [5, 10, 5, 10], [1, 1, 1, 1]]) == 115
    assert candidate(n = 12,k = 4,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1], [3, 4, 1, 2]]) == 72
    assert candidate(n = 15,k = 4,time = [[5, 1, 1, 5], [1, 5, 5, 1], [3, 3, 3, 3], [2, 2, 2, 2]]) == 86
    assert candidate(n = 7,k = 7,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7]]) == 93
    assert candidate(n = 25,k = 4,time = [[10, 10, 10, 10], [9, 9, 9, 9], [8, 8, 8, 8], [7, 7, 7, 7]]) == 462
    assert candidate(n = 20,k = 5,time = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2], [3, 1, 4, 1], [5, 5, 5, 5]]) == 156
    assert candidate(n = 18,k = 5,time = [[1, 1, 10, 1], [1, 1, 9, 1], [1, 1, 8, 1], [1, 1, 7, 1], [1, 1, 6, 1]]) == 189
    assert candidate(n = 12,k = 6,time = [[3, 2, 1, 2], [2, 2, 2, 2], [1, 2, 3, 2], [4, 2, 4, 2], [5, 2, 5, 2], [6, 2, 6, 2]]) == 132
    assert candidate(n = 8,k = 6,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4], [4, 5, 4, 5], [5, 6, 5, 6], [6, 7, 6, 7]]) == 84
    assert candidate(n = 50,k = 10,time = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]) == 903
    assert candidate(n = 20,k = 5,time = [[2, 3, 4, 5], [1, 2, 3, 4], [3, 1, 2, 1], [4, 4, 1, 3], [5, 5, 5, 5]]) == 145
    assert candidate(n = 20,k = 5,time = [[5, 2, 3, 2], [4, 3, 2, 5], [3, 5, 1, 3], [2, 4, 1, 4], [1, 6, 2, 6]]) == 140
    assert candidate(n = 10,k = 3,time = [[1, 2, 1, 2], [2, 3, 2, 3], [3, 4, 3, 4]]) == 52


