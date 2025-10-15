def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 0, 0, 0],cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],m = 5,n = 2,target = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 0, 0, 0],cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],m = 5,n = 2,target = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0],cost = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70], [50, 60, 70, 80]],m = 5,n = 4,target = 3) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0],cost = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70], [50, 60, 70, 80]],m = 5,n = 4,target = 3) == 160: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 2, 3, 4, 5],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 5,n = 5,target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 2, 3, 4, 5],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 5,n = 5,target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(houses = [3, 1, 2, 3],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 4,n = 3,target = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [3, 1, 2, 3],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 4,n = 3,target = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 1, 0, 0],cost = [[1, 2], [3, 4], [1, 2], [3, 4], [1, 2]],m = 5,n = 2,target = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 1, 0, 0],cost = [[1, 2], [3, 4], [1, 2], [3, 4], [1, 2]],m = 5,n = 2,target = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 1, 2, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 1, 2, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 1, 0, 0, 0],cost = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],m = 5,n = 2,target = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 1, 0, 0, 0],cost = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],m = 5,n = 2,target = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],m = 5,n = 3,target = 2) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],m = 5,n = 3,target = 2) == 36: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 6,n = 2,target = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 6,n = 2,target = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 2, 0, 3],cost = [[5, 8, 6], [19, 14, 13], [7, 5, 5], [3, 6, 14], [2, 11, 1]],m = 5,n = 3,target = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 2, 0, 3],cost = [[5, 8, 6], [19, 14, 13], [7, 5, 5], [3, 6, 14], [2, 11, 1]],m = 5,n = 3,target = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 3, 0, 2],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 5,n = 3,target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 3, 0, 2],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 5,n = 3,target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],m = 3,n = 3,target = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],m = 3,n = 3,target = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]],m = 5,n = 4,target = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]],m = 5,n = 4,target = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 0, 0, 1, 0, 0, 0, 0],cost = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30]],m = 10,n = 3,target = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 0, 0, 1, 0, 0, 0, 0],cost = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30]],m = 10,n = 3,target = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],m = 7,n = 5,target = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],m = 7,n = 5,target = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 7, 2, 8, 6], [5, 9, 1, 3, 4, 7], [9, 3, 5, 6, 2, 8], [8, 6, 9, 1, 7, 4], [7, 5, 8, 9, 3, 2], [6, 8, 4, 5, 9, 1], [3, 7, 9, 8, 6, 5], [2, 9, 6, 7, 4, 8], [8, 1, 4, 2, 9, 6], [6, 2, 8, 3, 1, 9]],m = 10,n = 6,target = 5) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 7, 2, 8, 6], [5, 9, 1, 3, 4, 7], [9, 3, 5, 6, 2, 8], [8, 6, 9, 1, 7, 4], [7, 5, 8, 9, 3, 2], [6, 8, 4, 5, 9, 1], [3, 7, 9, 8, 6, 5], [2, 9, 6, 7, 4, 8], [8, 1, 4, 2, 9, 6], [6, 2, 8, 3, 1, 9]],m = 10,n = 6,target = 5) == 22: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]],m = 8,n = 3,target = 4) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]],m = 8,n = 3,target = 4) == 31: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5]],m = 11,n = 3,target = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5]],m = 11,n = 3,target = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [1, 1, 1, 1, 1], [10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 6, 9, 12, 15], [15, 12, 9, 6, 3], [3, 2, 1, 4, 5], [5, 4, 3, 2, 1]],m = 15,n = 5,target = 7) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [1, 1, 1, 1, 1], [10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 6, 9, 12, 15], [15, 12, 9, 6, 3], [3, 2, 1, 4, 5], [5, 4, 3, 2, 1]],m = 15,n = 5,target = 7) == 53: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 3], [3, 2, 1], [2, 1, 4], [1, 3, 2], [4, 3, 1], [2, 1, 3], [3, 2, 4]],m = 7,n = 3,target = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 3], [3, 2, 1], [2, 1, 4], [1, 3, 2], [4, 3, 1], [2, 1, 3], [3, 2, 4]],m = 7,n = 3,target = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 0, 2, 0, 0, 0, 0, 0, 3],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3]],m = 10,n = 3,target = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 0, 2, 0, 0, 0, 0, 0, 3],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3]],m = 10,n = 3,target = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 3, 0, 1, 0, 2, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 8,n = 4,target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 3, 0, 1, 0, 2, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 8,n = 4,target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 9, 3, 5], [3, 4, 1, 10], [7, 8, 4, 5], [3, 2, 8, 5], [2, 6, 3, 7], [7, 1, 8, 3], [4, 2, 1, 4], [1, 4, 3, 9]],m = 8,n = 4,target = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 9, 3, 5], [3, 4, 1, 10], [7, 8, 4, 5], [3, 2, 8, 5], [2, 6, 3, 7], [7, 1, 8, 3], [4, 2, 1, 4], [1, 4, 3, 9]],m = 8,n = 4,target = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 2, 0, 2],cost = [[10, 20, 30, 40], [20, 30, 10, 40], [30, 10, 20, 40], [10, 40, 20, 30], [20, 30, 40, 10], [30, 40, 10, 20]],m = 6,n = 4,target = 3) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 2, 0, 2],cost = [[10, 20, 30, 40], [20, 30, 10, 40], [30, 10, 20, 40], [10, 40, 20, 30], [20, 30, 40, 10], [30, 40, 10, 20]],m = 6,n = 4,target = 3) == 40: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],cost = [[10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4]],m = 10,n = 4,target = 4) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],cost = [[10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4]],m = 10,n = 4,target = 4) == 45: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],m = 10,n = 10,target = 5) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],m = 10,n = 10,target = 5) == 57: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],m = 11,n = 11,target = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],m = 11,n = 11,target = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 3, 2, 1, 4], [3, 2, 1, 4, 5], [2, 1, 4, 5, 3], [1, 4, 5, 3, 2], [4, 5, 3, 2, 1], [5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [3, 2, 1, 5, 4], [2, 1, 5, 4, 3], [1, 5, 4, 3, 2]],m = 10,n = 5,target = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 3, 2, 1, 4], [3, 2, 1, 4, 5], [2, 1, 4, 5, 3], [1, 4, 5, 3, 2], [4, 5, 3, 2, 1], [5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [3, 2, 1, 5, 4], [2, 1, 5, 4, 3], [1, 5, 4, 3, 2]],m = 10,n = 5,target = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10], [8, 9, 10, 11], [9, 10, 11, 12], [10, 11, 12, 13]],m = 10,n = 4,target = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10], [8, 9, 10, 11], [9, 10, 11, 12], [10, 11, 12, 13]],m = 10,n = 4,target = 5) == 28: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 10, 10], [1, 2, 3], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 10,n = 3,target = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 10, 10], [1, 2, 3], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 10,n = 3,target = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2]],m = 15,n = 2,target = 7) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2]],m = 15,n = 2,target = 7) == 19: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 2, 0, 0, 0, 0],cost = [[4, 3, 1, 2], [9, 1, 4, 8], [5, 7, 9, 6], [1, 1, 5, 2], [8, 5, 3, 3], [4, 6, 1, 9], [2, 3, 7, 7], [7, 4, 8, 5]],m = 8,n = 4,target = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 2, 0, 0, 0, 0],cost = [[4, 3, 1, 2], [9, 1, 4, 8], [5, 7, 9, 6], [1, 1, 5, 2], [8, 5, 3, 3], [4, 6, 1, 9], [2, 3, 7, 7], [7, 4, 8, 5]],m = 8,n = 4,target = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 1, 0, 0, 0],cost = [[2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1]],m = 7,n = 3,target = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 1, 0, 0, 0],cost = [[2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1]],m = 7,n = 3,target = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 15], [15, 10], [20, 25], [25, 20], [30, 35], [35, 30], [40, 45], [45, 40]],m = 8,n = 2,target = 6) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 15], [15, 10], [20, 25], [25, 20], [30, 35], [35, 30], [40, 45], [45, 40]],m = 8,n = 2,target = 6) == 205: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[4, 8, 2], [1, 10, 9], [6, 4, 8], [10, 2, 9], [3, 7, 5], [8, 3, 2], [1, 6, 5], [2, 4, 3]],m = 8,n = 3,target = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[4, 8, 2], [1, 10, 9], [6, 4, 8], [10, 2, 9], [3, 7, 5], [8, 3, 2], [1, 6, 5], [2, 4, 3]],m = 8,n = 3,target = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5]],m = 8,n = 3,target = 5) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5]],m = 8,n = 3,target = 5) == 46: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 3, 0, 2, 0, 1, 0, 0],cost = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],m = 8,n = 4,target = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 3, 0, 2, 0, 1, 0, 0],cost = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],m = 8,n = 4,target = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0],cost = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]],m = 8,n = 3,target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0],cost = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]],m = 8,n = 3,target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 2, 1, 0, 0, 3],cost = [[10, 8, 6, 4, 2], [9, 7, 5, 3, 1], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [100, 90, 80, 70, 60], [30, 25, 20, 15, 10]],m = 7,n = 5,target = 4) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 2, 1, 0, 0, 3],cost = [[10, 8, 6, 4, 2], [9, 7, 5, 3, 1], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [100, 90, 80, 70, 60], [30, 25, 20, 15, 10]],m = 7,n = 5,target = 4) == 80: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]],m = 7,n = 3,target = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]],m = 7,n = 3,target = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]],m = 7,n = 4,target = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]],m = 7,n = 4,target = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 20,n = 2,target = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 20,n = 2,target = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 1, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2]],m = 6,n = 3,target = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 1, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2]],m = 6,n = 3,target = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],m = 10,n = 2,target = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],m = 10,n = 2,target = 5) == 28: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1]],m = 8,n = 4,target = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1]],m = 8,n = 4,target = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 3, 0, 0, 0, 0],cost = [[1, 3, 2], [3, 1, 4], [1, 2, 3], [3, 2, 1], [1, 3, 2], [3, 2, 1], [1, 2, 3]],m = 7,n = 3,target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 3, 0, 0, 0, 0],cost = [[1, 3, 2], [3, 1, 4], [1, 2, 3], [3, 2, 1], [1, 3, 2], [3, 2, 1], [1, 2, 3]],m = 7,n = 3,target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],cost = [[100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50]],m = 10,n = 3,target = 5) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],cost = [[100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50]],m = 10,n = 3,target = 5) == 250: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],m = 11,n = 10,target = 6) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],m = 11,n = 10,target = 6) == 66: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 2, 0, 3, 0, 4, 0],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 8,n = 5,target = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 2, 0, 3, 0, 4, 0],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 8,n = 5,target = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 1, 0, 2, 0, 0, 0],cost = [[1, 10, 100, 1000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000]],m = 7,n = 4,target = 3) == 1211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 1, 0, 2, 0, 0, 0],cost = [[1, 10, 100, 1000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000]],m = 7,n = 4,target = 3) == 1211: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 20,n = 2,target = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 20,n = 2,target = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 1, 2, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [4, 5, 6], [5, 6, 4], [6, 4, 5], [7, 8, 9]],m = 7,n = 3,target = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 1, 2, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [4, 5, 6], [5, 6, 4], [6, 4, 5], [7, 8, 9]],m = 7,n = 3,target = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[3, 2, 1, 8, 9], [7, 8, 6, 4, 5], [2, 4, 3, 1, 8], [9, 1, 5, 7, 3], [4, 9, 2, 3, 7], [5, 3, 8, 1, 4], [1, 7, 2, 8, 6], [8, 6, 4, 9, 2], [3, 1, 7, 2, 5]],m = 9,n = 5,target = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[3, 2, 1, 8, 9], [7, 8, 6, 4, 5], [2, 4, 3, 1, 8], [9, 1, 5, 7, 3], [4, 9, 2, 3, 7], [5, 3, 8, 1, 4], [1, 7, 2, 8, 6], [8, 6, 4, 9, 2], [3, 1, 7, 2, 5]],m = 9,n = 5,target = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 2, 0, 3, 0, 1, 0, 2],cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 9,n = 3,target = 6) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 2, 0, 3, 0, 1, 0, 2],cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 9,n = 3,target = 6) == 40: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 20,n = 4,target = 12) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 20,n = 4,target = 12) == 23: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 10,n = 3,target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 10,n = 3,target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 0, 0, 2, 0],cost = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]],m = 7,n = 3,target = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 0, 0, 2, 0],cost = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]],m = 7,n = 3,target = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]],m = 9,n = 9,target = 6) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]],m = 9,n = 9,target = 6) == 41: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 1, 0, 1, 0, 1],cost = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30]],m = 7,n = 3,target = 3) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 1, 0, 1, 0, 1],cost = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30]],m = 7,n = 3,target = 3) == 40: {e}')
    
    total += 1
    try:
        result = candidate(houses = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],cost = [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1]],m = 10,n = 2,target = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],cost = [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1]],m = 10,n = 2,target = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]],m = 10,n = 3,target = 5) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]],m = 10,n = 3,target = 5) == 57: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 15,n = 2,target = 8) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 15,n = 2,target = 8) == 15: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 2, 0, 1, 0, 3, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2], [1, 4, 3, 2], [2, 3, 4, 1], [4, 1, 2, 3]],m = 7,n = 4,target = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 2, 0, 1, 0, 3, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2], [1, 4, 3, 2], [2, 3, 4, 1], [4, 1, 2, 3]],m = 7,n = 4,target = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 2, 1, 9, 5, 6, 3, 8], [8, 7, 6, 3, 9, 1, 5, 4], [2, 1, 8, 7, 6, 9, 4, 3], [5, 6, 7, 8, 2, 1, 9, 4], [9, 4, 5, 6, 7, 8, 2, 1], [3, 9, 4, 5, 6, 7, 8, 2], [1, 3, 9, 4, 5, 6, 7, 8], [6, 1, 3, 9, 4, 5, 6, 7], [7, 6, 1, 3, 9, 4, 5, 6], [8, 7, 6, 1, 3, 9, 4, 5], [5, 8, 7, 6, 1, 3, 9, 4]],m = 11,n = 8,target = 6) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 2, 1, 9, 5, 6, 3, 8], [8, 7, 6, 3, 9, 1, 5, 4], [2, 1, 8, 7, 6, 9, 4, 3], [5, 6, 7, 8, 2, 1, 9, 4], [9, 4, 5, 6, 7, 8, 2, 1], [3, 9, 4, 5, 6, 7, 8, 2], [1, 3, 9, 4, 5, 6, 7, 8], [6, 1, 3, 9, 4, 5, 6, 7], [7, 6, 1, 3, 9, 4, 5, 6], [8, 7, 6, 1, 3, 9, 4, 5], [5, 8, 7, 6, 1, 3, 9, 4]],m = 11,n = 8,target = 6) == 21: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(houses = [1, 0, 0, 0, 0],cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],m = 5,n = 2,target = 2) == 15
    assert candidate(houses = [0, 0, 0, 0, 0],cost = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70], [50, 60, 70, 80]],m = 5,n = 4,target = 3) == 160
    assert candidate(houses = [1, 2, 3, 4, 5],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 5,n = 5,target = 5) == 0
    assert candidate(houses = [3, 1, 2, 3],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 4,n = 3,target = 3) == -1
    assert candidate(houses = [1, 0, 1, 0, 0],cost = [[1, 2], [3, 4], [1, 2], [3, 4], [1, 2]],m = 5,n = 2,target = 2) == 8
    assert candidate(houses = [0, 2, 1, 2, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 11
    assert candidate(houses = [0, 1, 0, 0, 0],cost = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],m = 5,n = 2,target = 2) == 5
    assert candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],m = 5,n = 3,target = 2) == 36
    assert candidate(houses = [0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 6,n = 2,target = 1) == 6
    assert candidate(houses = [1, 0, 2, 0, 3],cost = [[5, 8, 6], [19, 14, 13], [7, 5, 5], [3, 6, 14], [2, 11, 1]],m = 5,n = 3,target = 3) == 20
    assert candidate(houses = [1, 0, 3, 0, 2],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 5,n = 3,target = 3) == 2
    assert candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],m = 5,n = 2,target = 3) == 9
    assert candidate(houses = [0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],m = 3,n = 3,target = 2) == 13
    assert candidate(houses = [0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]],m = 5,n = 4,target = 2) == 16
    assert candidate(houses = [0, 2, 0, 0, 0, 1, 0, 0, 0, 0],cost = [[10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 20, 30]],m = 10,n = 3,target = 5) == 100
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],m = 7,n = 5,target = 7) == 7
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 7, 2, 8, 6], [5, 9, 1, 3, 4, 7], [9, 3, 5, 6, 2, 8], [8, 6, 9, 1, 7, 4], [7, 5, 8, 9, 3, 2], [6, 8, 4, 5, 9, 1], [3, 7, 9, 8, 6, 5], [2, 9, 6, 7, 4, 8], [8, 1, 4, 2, 9, 6], [6, 2, 8, 3, 1, 9]],m = 10,n = 6,target = 5) == 22
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]],m = 8,n = 3,target = 4) == 31
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5], [5, 1, 2], [2, 5, 1], [1, 2, 5]],m = 11,n = 3,target = 5) == 19
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [1, 1, 1, 1, 1], [10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2], [1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 6, 9, 12, 15], [15, 12, 9, 6, 3], [3, 2, 1, 4, 5], [5, 4, 3, 2, 1]],m = 15,n = 5,target = 7) == 53
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 4, 3], [3, 2, 1], [2, 1, 4], [1, 3, 2], [4, 3, 1], [2, 1, 3], [3, 2, 4]],m = 7,n = 3,target = 4) == 10
    assert candidate(houses = [1, 0, 0, 2, 0, 0, 0, 0, 0, 3],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3]],m = 10,n = 3,target = 6) == 9
    assert candidate(houses = [0, 3, 0, 1, 0, 2, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 8,n = 4,target = 5) == 6
    assert candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 9, 3, 5], [3, 4, 1, 10], [7, 8, 4, 5], [3, 2, 8, 5], [2, 6, 3, 7], [7, 1, 8, 3], [4, 2, 1, 4], [1, 4, 3, 9]],m = 8,n = 4,target = 5) == 11
    assert candidate(houses = [0, 2, 0, 2, 0, 2],cost = [[10, 20, 30, 40], [20, 30, 10, 40], [30, 10, 20, 40], [10, 40, 20, 30], [20, 30, 40, 10], [30, 40, 10, 20]],m = 6,n = 4,target = 3) == 40
    assert candidate(houses = [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],cost = [[10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4], [10, 20, 30, 40], [1, 2, 3, 4]],m = 10,n = 4,target = 4) == 45
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],m = 10,n = 10,target = 5) == 57
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],m = 11,n = 11,target = 3) == 11
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[5, 3, 2, 1, 4], [3, 2, 1, 4, 5], [2, 1, 4, 5, 3], [1, 4, 5, 3, 2], [4, 5, 3, 2, 1], [5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [3, 2, 1, 5, 4], [2, 1, 5, 4, 3], [1, 5, 4, 3, 2]],m = 10,n = 5,target = 4) == 16
    assert candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10], [8, 9, 10, 11], [9, 10, 11, 12], [10, 11, 12, 13]],m = 10,n = 4,target = 5) == 28
    assert candidate(houses = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 10, 10], [1, 2, 3], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 10,n = 3,target = 3) == 90
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2]],m = 15,n = 2,target = 7) == 19
    assert candidate(houses = [0, 0, 0, 2, 0, 0, 0, 0],cost = [[4, 3, 1, 2], [9, 1, 4, 8], [5, 7, 9, 6], [1, 1, 5, 2], [8, 5, 3, 3], [4, 6, 1, 9], [2, 3, 7, 7], [7, 4, 8, 5]],m = 8,n = 4,target = 4) == 20
    assert candidate(houses = [0, 0, 0, 1, 0, 0, 0],cost = [[2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1]],m = 7,n = 3,target = 4) == 8
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[10, 15], [15, 10], [20, 25], [25, 20], [30, 35], [35, 30], [40, 45], [45, 40]],m = 8,n = 2,target = 6) == 205
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[4, 8, 2], [1, 10, 9], [6, 4, 8], [10, 2, 9], [3, 7, 5], [8, 3, 2], [1, 6, 5], [2, 4, 3]],m = 8,n = 3,target = 3) == 24
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5], [5, 9, 7], [7, 5, 9], [9, 7, 5]],m = 8,n = 3,target = 5) == 46
    assert candidate(houses = [0, 3, 0, 2, 0, 1, 0, 0],cost = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],m = 8,n = 4,target = 4) == 5
    assert candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0],cost = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]],m = 8,n = 3,target = 3) == 6
    assert candidate(houses = [0, 0, 2, 1, 0, 0, 3],cost = [[10, 8, 6, 4, 2], [9, 7, 5, 3, 1], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [100, 90, 80, 70, 60], [30, 25, 20, 15, 10]],m = 7,n = 5,target = 4) == 80
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]],m = 7,n = 3,target = 4) == 30
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10]],m = 7,n = 4,target = 4) == 30
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 20,n = 2,target = 10) == 25
    assert candidate(houses = [0, 0, 1, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3], [2, 3, 1], [3, 1, 2]],m = 6,n = 3,target = 4) == 6
    assert candidate(houses = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],cost = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],m = 10,n = 2,target = 5) == 28
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13
    assert candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 4, 1]],m = 8,n = 4,target = 5) == 9
    assert candidate(houses = [0, 0, 3, 0, 0, 0, 0],cost = [[1, 3, 2], [3, 1, 4], [1, 2, 3], [3, 2, 1], [1, 3, 2], [3, 2, 1], [1, 2, 3]],m = 7,n = 3,target = 3) == 9
    assert candidate(houses = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],cost = [[100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50], [100, 100, 100], [50, 50, 50]],m = 10,n = 3,target = 5) == 250
    assert candidate(houses = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],m = 11,n = 10,target = 6) == 66
    assert candidate(houses = [1, 0, 2, 0, 3, 0, 4, 0],cost = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],m = 8,n = 5,target = 4) == 10
    assert candidate(houses = [0, 1, 0, 2, 0, 0, 0],cost = [[1, 10, 100, 1000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000], [10, 100, 1000, 10000], [100, 1000, 10000, 100000], [1000, 10000, 100000, 1000000]],m = 7,n = 4,target = 3) == 1211
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 20,n = 2,target = 10) == 20
    assert candidate(houses = [0, 1, 2, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [4, 5, 6], [5, 6, 4], [6, 4, 5], [7, 8, 9]],m = 7,n = 3,target = 5) == 21
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[3, 2, 1, 8, 9], [7, 8, 6, 4, 5], [2, 4, 3, 1, 8], [9, 1, 5, 7, 3], [4, 9, 2, 3, 7], [5, 3, 8, 1, 4], [1, 7, 2, 8, 6], [8, 6, 4, 9, 2], [3, 1, 7, 2, 5]],m = 9,n = 5,target = 4) == 24
    assert candidate(houses = [1, 0, 2, 0, 3, 0, 1, 0, 2],cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]],m = 9,n = 3,target = 6) == 40
    assert candidate(houses = [0, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]],m = 20,n = 4,target = 12) == 23
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],m = 10,n = 3,target = 10) == 10
    assert candidate(houses = [0, 2, 0, 0, 0, 2, 0],cost = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]],m = 7,n = 3,target = 3) == 25
    assert candidate(houses = [0, 0, 0, 1, 0, 0, 0, 0, 0],cost = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]],m = 9,n = 9,target = 6) == 41
    assert candidate(houses = [1, 0, 1, 0, 1, 0, 1],cost = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30]],m = 7,n = 3,target = 3) == 40
    assert candidate(houses = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],cost = [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1], [1, 10], [10, 1]],m = 10,n = 2,target = 5) == 32
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]],m = 10,n = 3,target = 5) == 57
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]],m = 10,n = 2,target = 5) == 13
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],m = 15,n = 2,target = 8) == 15
    assert candidate(houses = [0, 2, 0, 1, 0, 3, 0],cost = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2], [1, 4, 3, 2], [2, 3, 4, 1], [4, 1, 2, 3]],m = 7,n = 4,target = 5) == 4
    assert candidate(houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [[7, 2, 1, 9, 5, 6, 3, 8], [8, 7, 6, 3, 9, 1, 5, 4], [2, 1, 8, 7, 6, 9, 4, 3], [5, 6, 7, 8, 2, 1, 9, 4], [9, 4, 5, 6, 7, 8, 2, 1], [3, 9, 4, 5, 6, 7, 8, 2], [1, 3, 9, 4, 5, 6, 7, 8], [6, 1, 3, 9, 4, 5, 6, 7], [7, 6, 1, 3, 9, 4, 5, 6], [8, 7, 6, 1, 3, 9, 4, 5], [5, 8, 7, 6, 1, 3, 9, 4]],m = 11,n = 8,target = 6) == 21


