def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [5, 5, 5], [20, 20, 20]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [5, 5, 5], [20, 20, 20]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[38, 25, 45], [76, 35, 3]]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[38, 25, 45], [76, 35, 3]]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[100, 100, 1], [100, 100, 1], [100, 100, 1]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[100, 100, 1], [100, 100, 1], [100, 100, 1]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 2], [3, 4, 4], [5, 6, 6]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 2], [3, 4, 4], [5, 6, 6]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[100, 100, 100], [99, 99, 99], [98, 98, 98]]) == 297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[100, 100, 100], [99, 99, 99], [98, 98, 98]]) == 297: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [12, 11, 10], [15, 14, 13]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [12, 11, 10], [15, 14, 13]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [20, 20, 20], [15, 15, 15], [25, 25, 25], [30, 30, 30]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [20, 20, 20], [15, 15, 15], [25, 25, 25], [30, 30, 30]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[20, 20, 20], [20, 20, 15], [20, 15, 10], [15, 10, 5]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[20, 20, 20], [20, 20, 15], [20, 15, 10], [15, 10, 5]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[3, 4, 5], [1, 2, 6], [4, 5, 3], [5, 3, 4], [6, 2, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[3, 4, 5], [1, 2, 6], [4, 5, 3], [5, 3, 4], [6, 2, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 50, 50], [49, 49, 49], [48, 48, 48], [47, 47, 47], [46, 46, 46], [45, 45, 45], [44, 44, 44]]) == 329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 50, 50], [49, 49, 49], [48, 48, 48], [47, 47, 47], [46, 46, 46], [45, 45, 45], [44, 44, 44]]) == 329: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 1, 1], [9, 2, 2], [8, 3, 3], [7, 4, 4], [6, 5, 5], [5, 6, 6], [4, 7, 7], [3, 8, 8], [2, 9, 9], [1, 10, 10], [10, 9, 8], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 10], [1, 10, 9]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 1, 1], [9, 2, 2], [8, 3, 3], [7, 4, 4], [6, 5, 5], [5, 6, 6], [4, 7, 7], [3, 8, 8], [2, 9, 9], [1, 10, 10], [10, 9, 8], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 10], [1, 10, 9]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[20, 30, 40], [40, 30, 20], [10, 5, 15], [5, 10, 15]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[20, 30, 40], [40, 30, 20], [10, 5, 15], [5, 10, 15]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 3, 5], [1, 4, 6], [1, 5, 7], [2, 4, 8], [2, 5, 9], [3, 5, 11]]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 3, 5], [1, 4, 6], [1, 5, 7], [2, 4, 8], [2, 5, 9], [3, 5, 11]]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80]]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80]]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[60, 50, 40], [50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1]]) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[60, 50, 40], [50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1]]) == 215: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 3, 2], [2, 1, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 3, 2], [2, 1, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 2], [2, 2, 1], [2, 1, 2], [2, 2, 3], [3, 2, 2], [2, 3, 2]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 2], [2, 2, 1], [2, 1, 2], [2, 2, 3], [3, 2, 2], [2, 3, 2]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [15, 25, 40], [20, 30, 50], [25, 40, 60], [30, 50, 70]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [15, 25, 40], [20, 30, 50], [25, 40, 60], [30, 50, 70]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 11, 12], [12, 10, 11], [11, 12, 10], [10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 11, 12], [12, 10, 11], [11, 12, 10], [10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[3, 6, 5], [4, 4, 7], [5, 6, 7], [3, 5, 8], [2, 3, 4]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[3, 6, 5], [4, 4, 7], [5, 6, 7], [3, 5, 8], [2, 3, 4]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[99, 99, 99], [98, 98, 98], [97, 97, 97], [96, 96, 96], [95, 95, 95], [94, 94, 94]]) == 579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[99, 99, 99], [98, 98, 98], [97, 97, 97], [96, 96, 96], [95, 95, 95], [94, 94, 94]]) == 579: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[20, 30, 40], [10, 20, 30], [15, 25, 35], [5, 10, 15], [25, 35, 45]]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[20, 30, 40], [10, 20, 30], [15, 25, 35], [5, 10, 15], [25, 35, 45]]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[8, 8, 8], [9, 9, 9], [7, 7, 7], [6, 6, 6], [10, 10, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[8, 8, 8], [9, 9, 9], [7, 7, 7], [6, 6, 6], [10, 10, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 10, 10]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 10, 10]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [5, 15, 25], [40, 60, 70], [15, 25, 5]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [5, 15, 25], [40, 60, 70], [15, 25, 5]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[40, 50, 60], [20, 30, 40], [10, 20, 30], [5, 10, 15], [25, 35, 45]]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[40, 50, 60], [20, 30, 40], [10, 20, 30], [5, 10, 15], [25, 35, 45]]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 30, 20], [40, 25, 15], [60, 35, 25], [70, 40, 30], [80, 45, 35]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 30, 20], [40, 25, 15], [60, 35, 25], [70, 40, 30], [80, 45, 35]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 30, 10], [10, 30, 20], [30, 10, 20], [20, 10, 30]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 30, 10], [10, 30, 20], [30, 10, 20], [20, 10, 30]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [4, 5, 6], [6, 5, 4], [5, 4, 6], [6, 4, 5], [5, 6, 4], [4, 6, 5]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [4, 5, 6], [6, 5, 4], [5, 4, 6], [6, 4, 5], [5, 6, 4], [4, 6, 5]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[20, 20, 20], [19, 19, 19], [18, 18, 18], [17, 17, 17], [16, 16, 16], [15, 15, 15]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[20, 20, 20], [19, 19, 19], [18, 18, 18], [17, 17, 17], [16, 16, 16], [15, 15, 15]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 100], [1, 100, 1], [100, 1, 1], [1, 1, 50], [1, 50, 1], [50, 1, 1]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 100], [1, 100, 1], [100, 1, 1], [1, 1, 50], [1, 50, 1], [50, 1, 1]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 5, 5], [5, 5, 6], [5, 5, 7], [5, 5, 8], [5, 5, 9]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 5, 5], [5, 5, 6], [5, 5, 7], [5, 5, 8], [5, 5, 9]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[7, 8, 9], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[7, 8, 9], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [10, 10, 5], [10, 5, 10], [5, 10, 10], [10, 5, 5], [5, 10, 5], [5, 5, 10]]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [10, 10, 5], [10, 5, 10], [5, 10, 10], [10, 5, 5], [5, 10, 5], [5, 5, 10]]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [53, 37, 95], [23, 12, 45], [12, 45, 23]]) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [53, 37, 95], [23, 12, 45], [12, 45, 23]]) == 375: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [45, 45, 45], [60, 60, 60], [80, 80, 80]]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [45, 45, 45], [60, 60, 60], [80, 80, 80]]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 12, 2], [2, 9, 12], [12, 3, 4], [8, 6, 10], [7, 12, 5], [1, 15, 15], [15, 1, 15], [15, 15, 1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 12, 2], [2, 9, 12], [12, 3, 4], [8, 6, 10], [7, 12, 5], [1, 15, 15], [15, 1, 15], [15, 15, 1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 3, 1], [7, 5, 3], [9, 7, 5], [11, 9, 7], [13, 11, 9], [15, 13, 11]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 3, 1], [7, 5, 3], [9, 7, 5], [11, 9, 7], [13, 11, 9], [15, 13, 11]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[7, 3, 1], [8, 4, 2], [9, 5, 3], [10, 6, 4], [11, 7, 5], [12, 8, 6]]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[7, 3, 1], [8, 4, 2], [9, 5, 3], [10, 6, 4], [11, 7, 5], [12, 8, 6]]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35], [40, 40, 40], [45, 45, 45]]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35], [40, 40, 40], [45, 45, 45]]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[8, 1, 6], [3, 5, 7], [4, 9, 2], [2, 6, 8], [5, 7, 3], [9, 4, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[8, 1, 6], [3, 5, 7], [4, 9, 2], [2, 6, 8], [5, 7, 3], [9, 4, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[30, 20, 10], [25, 20, 10], [20, 15, 5], [15, 10, 5], [10, 6, 3], [5, 3, 1]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[30, 20, 10], [25, 20, 10], [20, 15, 5], [15, 10, 5], [10, 6, 3], [5, 3, 1]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [60, 60, 60], [10, 10, 10], [20, 20, 20], [30, 30, 30]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [60, 60, 60], [10, 10, 10], [20, 20, 20], [30, 30, 30]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 12, 17], [3, 8, 9], [1, 2, 3], [6, 7, 8], [4, 10, 11], [2, 5, 6]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 12, 17], [3, 8, 9], [1, 2, 3], [6, 7, 8], [4, 10, 11], [2, 5, 6]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[100, 1, 1], [99, 2, 2], [98, 3, 3], [97, 4, 4], [96, 5, 5], [95, 6, 6], [94, 7, 7], [93, 8, 8], [92, 9, 9], [91, 10, 10]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[100, 1, 1], [99, 2, 2], [98, 3, 3], [97, 4, 4], [96, 5, 5], [95, 6, 6], [94, 7, 7], [93, 8, 8], [92, 9, 9], [91, 10, 10]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[8, 8, 8], [7, 7, 9], [6, 6, 10], [5, 5, 11], [4, 4, 12], [3, 3, 13], [2, 2, 14], [1, 1, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[8, 8, 8], [7, 7, 9], [6, 6, 10], [5, 5, 11], [4, 4, 12], [3, 3, 13], [2, 2, 14], [1, 1, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[100, 50, 25], [50, 25, 12], [25, 12, 6], [12, 6, 3], [6, 3, 1], [3, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[100, 50, 25], [50, 25, 12], [25, 12, 6], [12, 6, 3], [6, 3, 1], [3, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32], [1, 1, 4]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32], [1, 1, 4]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[7, 11, 17], [11, 7, 17], [17, 11, 7], [7, 17, 11], [11, 17, 7], [17, 7, 11], [7, 11, 17], [11, 7, 17], [17, 11, 7]]) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[7, 11, 17], [11, 7, 17], [17, 11, 7], [7, 17, 11], [11, 17, 7], [17, 7, 11], [7, 11, 17], [11, 7, 17], [17, 11, 7]]) == 153: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[20, 20, 20], [10, 10, 10], [30, 30, 30], [15, 15, 15]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[20, 20, 20], [10, 10, 10], [30, 30, 30], [15, 15, 15]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 100], [2, 2, 99], [3, 3, 98], [4, 4, 97], [5, 5, 96], [6, 6, 95]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 100], [2, 2, 99], [3, 3, 98], [4, 4, 97], [5, 5, 96], [6, 6, 95]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[8, 8, 8], [8, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[8, 8, 8], [8, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 12, 3], [1, 3, 5], [6, 7, 8], [5, 4, 3], [7, 8, 9], [8, 9, 10]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 12, 3], [1, 3, 5], [6, 7, 8], [5, 4, 3], [7, 8, 9], [8, 9, 10]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[23, 28, 32], [28, 32, 23], [32, 23, 28], [11, 29, 31], [29, 31, 11], [31, 11, 29], [12, 16, 24], [16, 24, 12], [24, 12, 16], [16, 24, 14]]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[23, 28, 32], [28, 32, 23], [32, 23, 28], [11, 29, 31], [29, 31, 11], [31, 11, 29], [12, 16, 24], [16, 24, 12], [24, 12, 16], [16, 24, 14]]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[15, 12, 8], [8, 12, 15], [12, 15, 8], [9, 10, 7], [7, 10, 9], [10, 7, 9]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[15, 12, 8], [8, 12, 15], [12, 15, 8], [9, 10, 7], [7, 10, 9], [10, 7, 9]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 10], [1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 6, 5], [1, 7, 4], [1, 8, 3], [1, 9, 2], [1, 10, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 10], [1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 6, 5], [1, 7, 4], [1, 8, 3], [1, 9, 2], [1, 10, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[30, 50, 70], [20, 40, 60], [10, 30, 50], [5, 15, 25], [1, 2, 3]]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[30, 50, 70], [20, 40, 60], [10, 30, 50], [5, 15, 25], [1, 2, 3]]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[9, 18, 36], [18, 36, 72], [36, 72, 144], [72, 144, 288], [144, 288, 576], [288, 576, 1152]]) == 2268
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[9, 18, 36], [18, 36, 72], [36, 72, 144], [72, 144, 288], [144, 288, 576], [288, 576, 1152]]) == 2268: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[25, 15, 10], [15, 10, 5], [10, 5, 2], [5, 3, 1], [3, 2, 1], [2, 1, 1], [1, 1, 1]]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[25, 15, 10], [15, 10, 5], [10, 5, 2], [5, 3, 1], [3, 2, 1], [2, 1, 1], [1, 1, 1]]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[12, 34, 56], [34, 12, 78], [56, 78, 12], [78, 12, 34]]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[12, 34, 56], [34, 12, 78], [56, 78, 12], [78, 12, 34]]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[100, 1, 1], [1, 100, 1], [1, 1, 100], [99, 2, 2], [2, 99, 2], [2, 2, 99], [50, 50, 50], [75, 75, 75]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[100, 1, 1], [1, 100, 1], [1, 1, 100], [99, 2, 2], [2, 99, 2], [2, 2, 99], [50, 50, 50], [75, 75, 75]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[3, 4, 5], [3, 3, 3], [3, 5, 5], [2, 3, 4], [2, 2, 2], [1, 1, 1], [1, 2, 3]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[3, 4, 5], [3, 3, 3], [3, 5, 5], [2, 3, 4], [2, 2, 2], [1, 1, 1], [1, 2, 3]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[15, 10, 5], [10, 8, 4], [5, 4, 2], [30, 20, 10], [20, 15, 5], [10, 6, 3]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[15, 10, 5], [10, 8, 4], [5, 4, 2], [30, 20, 10], [20, 15, 5], [10, 6, 3]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 1, 1], [1, 2, 2], [2, 2, 2], [1, 3, 3], [2, 3, 3], [3, 3, 3], [1, 4, 4], [2, 4, 4], [3, 4, 4], [4, 4, 4]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 1, 1], [1, 2, 2], [2, 2, 2], [1, 3, 3], [2, 3, 3], [3, 3, 3], [1, 4, 4], [2, 4, 4], [3, 4, 4], [4, 4, 4]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30], [10, 30, 20], [30, 10, 20], [20, 30, 10]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30], [10, 30, 20], [30, 10, 20], [20, 30, 10]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[5, 20, 30], [20, 30, 5], [30, 5, 20], [5, 30, 20], [30, 20, 5], [20, 5, 30]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[5, 20, 30], [20, 30, 5], [30, 5, 20], [5, 30, 20], [30, 20, 5], [20, 5, 30]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[4, 5, 6], [6, 5, 4], [7, 8, 9], [9, 8, 7], [1, 2, 3], [3, 2, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[4, 5, 6], [6, 5, 4], [7, 8, 9], [9, 8, 7], [1, 2, 3], [3, 2, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[40, 40, 40], [30, 30, 30], [20, 20, 20], [10, 10, 10], [5, 5, 5], [1, 1, 1], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1]]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[40, 40, 40], [30, 30, 30], [20, 20, 20], [10, 10, 10], [5, 5, 5], [1, 1, 1], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1]]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70], [60, 70, 80], [70, 80, 90], [80, 90, 100]]) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70], [60, 70, 80], [70, 80, 90], [80, 90, 100]]) == 520: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]) == 48
    assert candidate(cuboids = [[10, 10, 10], [5, 5, 5], [20, 20, 20]]) == 35
    assert candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 6
    assert candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]) == 190
    assert candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18
    assert candidate(cuboids = [[38, 25, 45], [76, 35, 3]]) == 76
    assert candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6]]) == 40
    assert candidate(cuboids = [[100, 100, 1], [100, 100, 1], [100, 100, 1]]) == 300
    assert candidate(cuboids = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 4
    assert candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 10
    assert candidate(cuboids = [[1, 2, 2], [3, 4, 4], [5, 6, 6]]) == 12
    assert candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7]]) == 34
    assert candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8]]) == 27
    assert candidate(cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]) == 102
    assert candidate(cuboids = [[1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 300
    assert candidate(cuboids = [[100, 100, 100], [99, 99, 99], [98, 98, 98]]) == 297
    assert candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30]]) == 90
    assert candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60]]) == 210
    assert candidate(cuboids = [[3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11]]) == 56
    assert candidate(cuboids = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [12, 11, 10], [15, 14, 13]]) == 45
    assert candidate(cuboids = [[10, 10, 10], [20, 20, 20], [15, 15, 15], [25, 25, 25], [30, 30, 30]]) == 100
    assert candidate(cuboids = [[20, 20, 20], [20, 20, 15], [20, 15, 10], [15, 10, 5]]) == 75
    assert candidate(cuboids = [[3, 4, 5], [1, 2, 6], [4, 5, 3], [5, 3, 4], [6, 2, 1]]) == 15
    assert candidate(cuboids = [[50, 50, 50], [49, 49, 49], [48, 48, 48], [47, 47, 47], [46, 46, 46], [45, 45, 45], [44, 44, 44]]) == 329
    assert candidate(cuboids = [[10, 1, 1], [9, 2, 2], [8, 3, 3], [7, 4, 4], [6, 5, 5], [5, 6, 6], [4, 7, 7], [3, 8, 8], [2, 9, 9], [1, 10, 10], [10, 9, 8], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 10], [1, 10, 9]]) == 64
    assert candidate(cuboids = [[30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 70
    assert candidate(cuboids = [[20, 30, 40], [40, 30, 20], [10, 5, 15], [5, 10, 15]]) == 110
    assert candidate(cuboids = [[1, 3, 5], [1, 4, 6], [1, 5, 7], [2, 4, 8], [2, 5, 9], [3, 5, 11]]) == 39
    assert candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55
    assert candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80]]) == 360
    assert candidate(cuboids = [[60, 50, 40], [50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 2], [5, 2, 1]]) == 215
    assert candidate(cuboids = [[1, 3, 2], [2, 1, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33
    assert candidate(cuboids = [[1, 2, 2], [2, 2, 1], [2, 1, 2], [2, 2, 3], [3, 2, 2], [2, 3, 2]]) == 15
    assert candidate(cuboids = [[10, 20, 30], [15, 25, 40], [20, 30, 50], [25, 40, 60], [30, 50, 70]]) == 250
    assert candidate(cuboids = [[10, 11, 12], [12, 10, 11], [11, 12, 10], [10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40]]) == 136
    assert candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1]]) == 18
    assert candidate(cuboids = [[3, 6, 5], [4, 4, 7], [5, 6, 7], [3, 5, 8], [2, 3, 4]]) == 18
    assert candidate(cuboids = [[99, 99, 99], [98, 98, 98], [97, 97, 97], [96, 96, 96], [95, 95, 95], [94, 94, 94]]) == 579
    assert candidate(cuboids = [[50, 40, 30], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1], [9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 165
    assert candidate(cuboids = [[20, 30, 40], [10, 20, 30], [15, 25, 35], [5, 10, 15], [25, 35, 45]]) == 165
    assert candidate(cuboids = [[8, 8, 8], [9, 9, 9], [7, 7, 7], [6, 6, 6], [10, 10, 10]]) == 40
    assert candidate(cuboids = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 10, 10]]) == 100
    assert candidate(cuboids = [[10, 20, 30], [5, 15, 25], [40, 60, 70], [15, 25, 5]]) == 150
    assert candidate(cuboids = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 30
    assert candidate(cuboids = [[40, 50, 60], [20, 30, 40], [10, 20, 30], [5, 10, 15], [25, 35, 45]]) == 190
    assert candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 22
    assert candidate(cuboids = [[50, 30, 20], [40, 25, 15], [60, 35, 25], [70, 40, 30], [80, 45, 35]]) == 300
    assert candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 30, 10], [10, 30, 20], [30, 10, 20], [20, 10, 30]]) == 180
    assert candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [4, 5, 6], [6, 5, 4], [5, 4, 6], [6, 4, 5], [5, 6, 4], [4, 6, 5]]) == 54
    assert candidate(cuboids = [[20, 20, 20], [19, 19, 19], [18, 18, 18], [17, 17, 17], [16, 16, 16], [15, 15, 15]]) == 105
    assert candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50]]) == 150
    assert candidate(cuboids = [[1, 1, 100], [1, 100, 1], [100, 1, 1], [1, 1, 50], [1, 50, 1], [50, 1, 1]]) == 450
    assert candidate(cuboids = [[5, 5, 5], [5, 5, 6], [5, 5, 7], [5, 5, 8], [5, 5, 9]]) == 35
    assert candidate(cuboids = [[7, 8, 9], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]]) == 71
    assert candidate(cuboids = [[10, 10, 10], [10, 10, 5], [10, 5, 10], [5, 10, 10], [10, 5, 5], [5, 10, 5], [5, 5, 10]]) == 70
    assert candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [53, 37, 95], [23, 12, 45], [12, 45, 23]]) == 375
    assert candidate(cuboids = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [45, 45, 45], [60, 60, 60], [80, 80, 80]]) == 270
    assert candidate(cuboids = [[5, 12, 2], [2, 9, 12], [12, 3, 4], [8, 6, 10], [7, 12, 5], [1, 15, 15], [15, 1, 15], [15, 15, 1]]) == 45
    assert candidate(cuboids = [[5, 3, 1], [7, 5, 3], [9, 7, 5], [11, 9, 7], [13, 11, 9], [15, 13, 11]]) == 60
    assert candidate(cuboids = [[7, 3, 1], [8, 4, 2], [9, 5, 3], [10, 6, 4], [11, 7, 5], [12, 8, 6]]) == 57
    assert candidate(cuboids = [[10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35], [40, 40, 40], [45, 45, 45]]) == 220
    assert candidate(cuboids = [[8, 1, 6], [3, 5, 7], [4, 9, 2], [2, 6, 8], [5, 7, 3], [9, 4, 1]]) == 18
    assert candidate(cuboids = [[30, 20, 10], [25, 20, 10], [20, 15, 5], [15, 10, 5], [10, 6, 3], [5, 3, 1]]) == 105
    assert candidate(cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12], [60, 60, 60], [10, 10, 10], [20, 20, 20], [30, 30, 30]]) == 200
    assert candidate(cuboids = [[5, 12, 17], [3, 8, 9], [1, 2, 3], [6, 7, 8], [4, 10, 11], [2, 5, 6]]) == 46
    assert candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2]]) == 18
    assert candidate(cuboids = [[100, 1, 1], [99, 2, 2], [98, 3, 3], [97, 4, 4], [96, 5, 5], [95, 6, 6], [94, 7, 7], [93, 8, 8], [92, 9, 9], [91, 10, 10]]) == 100
    assert candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 30
    assert candidate(cuboids = [[8, 8, 8], [7, 7, 9], [6, 6, 10], [5, 5, 11], [4, 4, 12], [3, 3, 13], [2, 2, 14], [1, 1, 15]]) == 15
    assert candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70]]) == 250
    assert candidate(cuboids = [[100, 50, 25], [50, 25, 12], [25, 12, 6], [12, 6, 3], [6, 3, 1], [3, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 199
    assert candidate(cuboids = [[10, 20, 30], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 57
    assert candidate(cuboids = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32], [1, 1, 4]]) == 49
    assert candidate(cuboids = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]) == 21
    assert candidate(cuboids = [[7, 11, 17], [11, 7, 17], [17, 11, 7], [7, 17, 11], [11, 17, 7], [17, 7, 11], [7, 11, 17], [11, 7, 17], [17, 11, 7]]) == 153
    assert candidate(cuboids = [[20, 20, 20], [10, 10, 10], [30, 30, 30], [15, 15, 15]]) == 75
    assert candidate(cuboids = [[1, 1, 100], [2, 2, 99], [3, 3, 98], [4, 4, 97], [5, 5, 96], [6, 6, 95]]) == 100
    assert candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]) == 33
    assert candidate(cuboids = [[8, 8, 8], [8, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 49
    assert candidate(cuboids = [[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 52
    assert candidate(cuboids = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]) == 18
    assert candidate(cuboids = [[10, 12, 3], [1, 3, 5], [6, 7, 8], [5, 4, 3], [7, 8, 9], [8, 9, 10]]) == 37
    assert candidate(cuboids = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 40
    assert candidate(cuboids = [[9, 8, 7], [8, 7, 6], [7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1]]) == 42
    assert candidate(cuboids = [[23, 28, 32], [28, 32, 23], [32, 23, 28], [11, 29, 31], [29, 31, 11], [31, 11, 29], [12, 16, 24], [16, 24, 12], [24, 12, 16], [16, 24, 14]]) == 192
    assert candidate(cuboids = [[15, 12, 8], [8, 12, 15], [12, 15, 8], [9, 10, 7], [7, 10, 9], [10, 7, 9]]) == 75
    assert candidate(cuboids = [[1, 1, 10], [1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 6, 5], [1, 7, 4], [1, 8, 3], [1, 9, 2], [1, 10, 1]]) == 20
    assert candidate(cuboids = [[30, 50, 70], [20, 40, 60], [10, 30, 50], [5, 15, 25], [1, 2, 3]]) == 208
    assert candidate(cuboids = [[9, 18, 36], [18, 36, 72], [36, 72, 144], [72, 144, 288], [144, 288, 576], [288, 576, 1152]]) == 2268
    assert candidate(cuboids = [[25, 15, 10], [15, 10, 5], [10, 5, 2], [5, 3, 1], [3, 2, 1], [2, 1, 1], [1, 1, 1]]) == 61
    assert candidate(cuboids = [[12, 34, 56], [34, 12, 78], [56, 78, 12], [78, 12, 34]]) == 290
    assert candidate(cuboids = [[100, 1, 1], [1, 100, 1], [1, 1, 100], [99, 2, 2], [2, 99, 2], [2, 2, 99], [50, 50, 50], [75, 75, 75]]) == 300
    assert candidate(cuboids = [[3, 4, 5], [3, 3, 3], [3, 5, 5], [2, 3, 4], [2, 2, 2], [1, 1, 1], [1, 2, 3]]) == 18
    assert candidate(cuboids = [[15, 10, 5], [10, 8, 4], [5, 4, 2], [30, 20, 10], [20, 15, 5], [10, 6, 3]]) == 90
    assert candidate(cuboids = [[5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 18
    assert candidate(cuboids = [[1, 1, 1], [1, 2, 2], [2, 2, 2], [1, 3, 3], [2, 3, 3], [3, 3, 3], [1, 4, 4], [2, 4, 4], [3, 4, 4], [4, 4, 4]]) == 22
    assert candidate(cuboids = [[10, 20, 30], [30, 20, 10], [20, 10, 30], [10, 30, 20], [30, 10, 20], [20, 30, 10]]) == 180
    assert candidate(cuboids = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25]]) == 75
    assert candidate(cuboids = [[5, 20, 30], [20, 30, 5], [30, 5, 20], [5, 30, 20], [30, 20, 5], [20, 5, 30]]) == 180
    assert candidate(cuboids = [[10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 55
    assert candidate(cuboids = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) == 26
    assert candidate(cuboids = [[4, 5, 6], [6, 5, 4], [7, 8, 9], [9, 8, 7], [1, 2, 3], [3, 2, 1]]) == 36
    assert candidate(cuboids = [[40, 40, 40], [30, 30, 30], [20, 20, 20], [10, 10, 10], [5, 5, 5], [1, 1, 1], [40, 30, 20], [30, 20, 10], [20, 10, 5], [10, 5, 1]]) == 141
    assert candidate(cuboids = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45
    assert candidate(cuboids = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 42
    assert candidate(cuboids = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]) == 108
    assert candidate(cuboids = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 550
    assert candidate(cuboids = [[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70], [60, 70, 80], [70, 80, 90], [80, 90, 100]]) == 520


