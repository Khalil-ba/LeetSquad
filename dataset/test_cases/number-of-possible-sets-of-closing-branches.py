def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,maxDistance = 10,roads = []) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,maxDistance = 10,roads = []) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,maxDistance = 1,roads = [[0, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,maxDistance = 1,roads = [[0, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 15,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 5, 3], [5, 0, 3]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 15,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 5, 3], [5, 0, 3]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,maxDistance = 5,roads = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxDistance = 5,roads = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 6,roads = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [3, 4, 4]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 6,roads = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [3, 4, 4]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 15,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [0, 3, 15]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 15,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [0, 3, 15]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxDistance = 15,roads = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 4, 2], [1, 5, 3], [2, 4, 4], [2, 6, 5], [3, 5, 1], [3, 7, 2], [4, 6, 3], [4, 8, 4], [5, 7, 6], [6, 8, 7], [7, 8, 1]]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxDistance = 15,roads = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 4, 2], [1, 5, 3], [2, 4, 4], [2, 6, 5], [3, 5, 1], [3, 7, 2], [4, 6, 3], [4, 8, 4], [5, 7, 6], [6, 8, 7], [7, 8, 1]]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1]]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1]]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 1, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 1, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 0, 9], [4, 1, 10], [5, 2, 11]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 0, 9], [4, 1, 10], [5, 2, 11]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 12,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 3], [1, 4, 4], [2, 5, 5], [3, 6, 6], [4, 0, 1], [5, 1, 2], [6, 2, 3]]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 12,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 3], [1, 4, 4], [2, 5, 5], [3, 6, 6], [4, 0, 1], [5, 1, 2], [6, 2, 3]]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [0, 2, 3], [1, 2, 2], [1, 3, 2], [2, 3, 3]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [0, 2, 3], [1, 2, 2], [1, 3, 2], [2, 3, 3]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 6, 2], [4, 7, 2], [5, 8, 2], [6, 9, 2], [7, 0, 2], [8, 1, 2], [9, 2, 2]]) == 807
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 6, 2], [4, 7, 2], [5, 8, 2], [6, 9, 2], [7, 0, 2], [8, 1, 2], [9, 2, 2]]) == 807: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 0, 14], [5, 1, 15], [6, 2, 16], [7, 3, 17], [8, 4, 18]]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 0, 14], [5, 1, 15], [6, 2, 16], [7, 3, 17], [8, 4, 18]]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 4, 9], [1, 5, 10], [2, 6, 11], [3, 7, 12], [4, 0, 13], [5, 1, 14], [6, 2, 15], [7, 3, 16]]) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 4, 9], [1, 5, 10], [2, 6, 11], [3, 7, 12], [4, 0, 13], [5, 1, 14], [6, 2, 15], [7, 3, 16]]) == 137: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 12,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 2], [6, 0, 1], [0, 3, 2], [2, 4, 3], [1, 5, 2]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 12,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 2], [6, 0, 1], [0, 3, 2], [2, 4, 3], [1, 5, 2]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 4, 4], [4, 0, 3], [1, 4, 1], [2, 4, 2], [0, 3, 2]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 4, 4], [4, 0, 3], [1, 4, 1], [2, 4, 2], [0, 3, 2]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 4], [3, 4, 5], [4, 0, 6], [1, 3, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 4], [3, 4, 5], [4, 0, 6], [1, 3, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 1]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 1]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 2,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 2,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 1], [0, 3, 4], [2, 4, 1], [1, 3, 2]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 1], [0, 3, 4], [2, 4, 1], [1, 3, 2]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 3]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 3]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 8,roads = [[0, 1, 2], [0, 3, 5], [0, 4, 8], [1, 2, 3], [1, 5, 6], [2, 6, 4], [3, 4, 2], [3, 5, 1], [4, 6, 7], [5, 7, 2], [6, 7, 3]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 8,roads = [[0, 1, 2], [0, 3, 5], [0, 4, 8], [1, 2, 3], [1, 5, 6], [2, 6, 4], [3, 4, 2], [3, 5, 1], [4, 6, 7], [5, 7, 2], [6, 7, 3]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 2, 1], [1, 3, 1], [0, 3, 1], [2, 1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 2, 1], [1, 3, 1], [0, 3, 1], [2, 1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 7,roads = [[0, 1, 10], [0, 2, 15], [0, 3, 20], [0, 4, 25], [1, 2, 5], [1, 3, 10], [1, 4, 15], [2, 3, 5], [2, 4, 10], [3, 4, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 7,roads = [[0, 1, 10], [0, 2, 15], [0, 3, 20], [0, 4, 25], [1, 2, 5], [1, 3, 10], [1, 4, 15], [2, 3, 5], [2, 4, 10], [3, 4, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 0, 5], [0, 3, 3], [1, 4, 2], [2, 5, 4]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 0, 5], [0, 3, 3], [1, 4, 2], [2, 5, 4]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 0, 1], [0, 2, 1], [1, 3, 2], [2, 4, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 0, 1], [0, 2, 1], [1, 3, 2], [2, 4, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 0, 50]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 0, 50]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10], [3, 6, 11], [4, 0, 12], [5, 1, 13], [6, 2, 14]]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10], [3, 6, 11], [4, 0, 12], [5, 1, 13], [6, 2, 14]]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 6, 11], [1, 7, 12], [2, 8, 13], [3, 9, 14], [4, 0, 15], [5, 1, 16], [6, 2, 17], [7, 3, 18], [8, 4, 19], [9, 5, 20]]) == 573
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 6, 11], [1, 7, 12], [2, 8, 13], [3, 9, 14], [4, 0, 15], [5, 1, 16], [6, 2, 17], [7, 3, 18], [8, 4, 19], [9, 5, 20]]) == 573: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 2, 1], [1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 1, 8], [8, 2, 9]]) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 2, 1], [1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 1, 8], [8, 2, 9]]) == 245: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 4], [3, 4, 2], [4, 0, 5]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 4], [3, 4, 2], [4, 0, 5]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [2, 4, 2], [3, 4, 2], [3, 5, 1], [4, 5, 3]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [2, 4, 2], [3, 4, 2], [3, 5, 1], [4, 5, 3]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 3, 1], [1, 4, 1], [2, 0, 1], [3, 1, 1], [4, 2, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 3, 1], [1, 4, 1], [2, 0, 1], [3, 1, 1], [4, 2, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 0, 25], [0, 3, 1], [1, 4, 6]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 0, 25], [0, 3, 1], [1, 4, 6]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 1], [1, 4, 1], [2, 5, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 1], [1, 4, 1], [2, 5, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 0, 5], [0, 2, 1], [1, 3, 1], [2, 0, 1], [3, 1, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 0, 5], [0, 2, 1], [1, 3, 1], [2, 0, 1], [3, 1, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 2], [1, 3, 3], [2, 0, 3], [3, 1, 4]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 2], [1, 3, 3], [2, 0, 3], [3, 1, 4]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxDistance = 20,roads = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 5, 6], [1, 6, 7], [2, 6, 8], [2, 7, 9], [3, 7, 10], [3, 8, 11], [4, 8, 12], [4, 9, 13], [5, 9, 14], [6, 9, 15], [7, 9, 16], [8, 9, 17]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxDistance = 20,roads = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 5, 6], [1, 6, 7], [2, 6, 8], [2, 7, 9], [3, 7, 10], [3, 8, 11], [4, 8, 12], [4, 9, 13], [5, 9, 14], [6, 9, 15], [7, 9, 16], [8, 9, 17]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [0, 2, 5], [1, 3, 2], [2, 3, 4], [3, 4, 1]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [0, 2, 5], [1, 3, 2], [2, 3, 4], [3, 4, 1]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 6], [2, 3, 7], [3, 4, 8], [4, 5, 9], [5, 6, 10], [6, 0, 11], [0, 4, 3], [1, 5, 4], [2, 6, 5]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 6], [2, 3, 7], [3, 4, 8], [4, 5, 9], [5, 6, 10], [6, 0, 11], [0, 4, 3], [1, 5, 4], [2, 6, 5]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 0, 2], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 0, 2], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 0, 1], [7, 1, 1]]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 0, 1], [7, 1, 1]]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 0, 2], [4, 1, 2], [5, 2, 2]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 0, 2], [4, 1, 2], [5, 2, 2]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 3,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 3,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 1], [3, 7, 2], [4, 8, 5], [5, 9, 3], [6, 9, 6], [7, 8, 1], [8, 9, 2], [0, 3, 2], [1, 5, 1], [2, 4, 5]]) == 474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 1], [3, 7, 2], [4, 8, 5], [5, 9, 3], [6, 9, 6], [7, 8, 1], [8, 9, 2], [0, 3, 2], [1, 5, 1], [2, 4, 5]]) == 474: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 0, 3]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 0, 3]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 12,roads = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 4, 5], [3, 4, 2], [3, 5, 6], [4, 6, 3], [5, 6, 1]]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 12,roads = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 4, 5], [3, 4, 2], [3, 5, 6], [4, 6, 3], [5, 6, 1]]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxDistance = 25,roads = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 0, 11], [0, 4, 2], [1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 0, 7], [6, 1, 8], [7, 2, 9], [8, 3, 10]]) == 329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxDistance = 25,roads = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 0, 11], [0, 4, 2], [1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 0, 7], [6, 1, 8], [7, 2, 9], [8, 3, 10]]) == 329: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 1], [3, 4, 2], [4, 0, 3]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 1], [3, 4, 2], [4, 0, 3]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 3], [4, 5, 4], [5, 0, 4]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 3], [4, 5, 4], [5, 0, 4]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 0, 5], [5, 1, 6], [6, 2, 7]]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 0, 5], [5, 1, 6], [6, 2, 7]]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 7,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 7,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 2], [1, 3, 3], [2, 4, 4], [3, 5, 5], [4, 6, 6], [5, 7, 7]]) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 2], [1, 3, 3], [2, 4, 4], [3, 5, 5], [4, 6, 6], [5, 7, 7]]) == 167: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 1], [4, 0, 1]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 1], [4, 0, 1]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [4, 5, 5], [5, 6, 5], [6, 4, 5], [4, 6, 3], [5, 4, 4]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [4, 5, 5], [5, 6, 5], [6, 4, 5], [4, 6, 3], [5, 4, 4]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 0, 6], [4, 1, 7]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 0, 6], [4, 1, 7]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 4, 2], [4, 5, 3]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 4, 2], [4, 5, 3]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 5, 3], [5, 6, 3], [6, 0, 4]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 5, 3], [5, 6, 3], [6, 0, 4]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 9,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 5, 6]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 9,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 5, 6]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8], [3, 0, 9], [4, 1, 10]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8], [3, 0, 9], [4, 1, 10]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9], [0, 5, 5], [1, 6, 6], [2, 7, 7], [3, 0, 0]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9], [0, 5, 5], [1, 6, 6], [2, 7, 7], [3, 0, 0]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 0, 5]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 0, 5]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]) == 5
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5]]) == 20
    assert candidate(n = 1,maxDistance = 10,roads = []) == 2
    assert candidate(n = 2,maxDistance = 1,roads = [[0, 1, 1]]) == 4
    assert candidate(n = 4,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1]]) == 14
    assert candidate(n = 6,maxDistance = 15,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 5, 3], [5, 0, 3]]) == 32
    assert candidate(n = 3,maxDistance = 5,roads = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]) == 7
    assert candidate(n = 5,maxDistance = 6,roads = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [3, 4, 4]]) == 11
    assert candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 10
    assert candidate(n = 4,maxDistance = 15,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [0, 3, 15]]) == 12
    assert candidate(n = 4,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]]) == 9
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8]]) == 13
    assert candidate(n = 9,maxDistance = 15,roads = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 4, 2], [1, 5, 3], [2, 4, 4], [2, 6, 5], [3, 5, 1], [3, 7, 2], [4, 6, 3], [4, 8, 4], [5, 7, 6], [6, 8, 7], [7, 8, 1]]) == 198
    assert candidate(n = 8,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1]]) == 58
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 1, 3]]) == 30
    assert candidate(n = 6,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 0, 9], [4, 1, 10], [5, 2, 11]]) == 43
    assert candidate(n = 5,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1]]) == 29
    assert candidate(n = 7,maxDistance = 12,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 3], [1, 4, 4], [2, 5, 5], [3, 6, 6], [4, 0, 1], [5, 1, 2], [6, 2, 3]]) == 109
    assert candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [0, 2, 3], [1, 2, 2], [1, 3, 2], [2, 3, 3]]) == 14
    assert candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 6, 2], [4, 7, 2], [5, 8, 2], [6, 9, 2], [7, 0, 2], [8, 1, 2], [9, 2, 2]]) == 807
    assert candidate(n = 9,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 0, 14], [5, 1, 15], [6, 2, 16], [7, 3, 17], [8, 4, 18]]) == 252
    assert candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 4, 9], [1, 5, 10], [2, 6, 11], [3, 7, 12], [4, 0, 13], [5, 1, 14], [6, 2, 15], [7, 3, 16]]) == 137
    assert candidate(n = 7,maxDistance = 12,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 2], [6, 0, 1], [0, 3, 2], [2, 4, 3], [1, 5, 2]]) == 87
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 4, 4], [4, 0, 3], [1, 4, 1], [2, 4, 2], [0, 3, 2]]) == 28
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6]]) == 17
    assert candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 2], [2, 3, 4], [3, 4, 5], [4, 0, 6], [1, 3, 1]]) == 18
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3]]) == 52
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 1]]) == 23
    assert candidate(n = 4,maxDistance = 2,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]]) == 7
    assert candidate(n = 6,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 1], [0, 3, 4], [2, 4, 1], [1, 3, 2]]) == 50
    assert candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 0, 3]]) == 23
    assert candidate(n = 8,maxDistance = 8,roads = [[0, 1, 2], [0, 3, 5], [0, 4, 8], [1, 2, 3], [1, 5, 6], [2, 6, 4], [3, 4, 2], [3, 5, 1], [4, 6, 7], [5, 7, 2], [6, 7, 3]]) == 41
    assert candidate(n = 4,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 2, 1], [1, 3, 1], [0, 3, 1], [2, 1, 1]]) == 16
    assert candidate(n = 5,maxDistance = 7,roads = [[0, 1, 10], [0, 2, 15], [0, 3, 20], [0, 4, 25], [1, 2, 5], [1, 3, 10], [1, 4, 15], [2, 3, 5], [2, 4, 10], [3, 4, 5]]) == 9
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 0, 5], [0, 3, 3], [1, 4, 2], [2, 5, 4]]) == 56
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 0, 1], [0, 2, 1], [1, 3, 2], [2, 4, 3]]) == 30
    assert candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7]]) == 20
    assert candidate(n = 5,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 0, 50]]) == 7
    assert candidate(n = 7,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10], [3, 6, 11], [4, 0, 12], [5, 1, 13], [6, 2, 14]]) == 85
    assert candidate(n = 10,maxDistance = 30,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10], [0, 6, 11], [1, 7, 12], [2, 8, 13], [3, 9, 14], [4, 0, 15], [5, 1, 16], [6, 2, 17], [7, 3, 18], [8, 4, 19], [9, 5, 20]]) == 573
    assert candidate(n = 9,maxDistance = 15,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 0, 9], [0, 2, 1], [1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 1, 8], [8, 2, 9]]) == 245
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 4], [3, 4, 2], [4, 0, 5]]) == 21
    assert candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [2, 4, 2], [3, 4, 2], [3, 5, 1], [4, 5, 3]]) == 35
    assert candidate(n = 5,maxDistance = 3,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 3, 1], [1, 4, 1], [2, 0, 1], [3, 1, 1], [4, 2, 1]]) == 32
    assert candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 0, 25], [0, 3, 1], [1, 4, 6]]) == 21
    assert candidate(n = 6,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 1], [1, 4, 1], [2, 5, 1]]) == 56
    assert candidate(n = 4,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 0, 5], [0, 2, 1], [1, 3, 1], [2, 0, 1], [3, 1, 1]]) == 14
    assert candidate(n = 5,maxDistance = 6,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
    assert candidate(n = 4,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 2], [1, 3, 3], [2, 0, 3], [3, 1, 4]]) == 16
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5]]) == 11
    assert candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 29
    assert candidate(n = 10,maxDistance = 20,roads = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 5, 6], [1, 6, 7], [2, 6, 8], [2, 7, 9], [3, 7, 10], [3, 8, 11], [4, 8, 12], [4, 9, 13], [5, 9, 14], [6, 9, 15], [7, 9, 16], [8, 9, 17]]) == 120
    assert candidate(n = 5,maxDistance = 10,roads = [[0, 1, 3], [0, 2, 5], [1, 3, 2], [2, 3, 4], [3, 4, 1]]) == 22
    assert candidate(n = 7,maxDistance = 20,roads = [[0, 1, 5], [1, 2, 6], [2, 3, 7], [3, 4, 8], [4, 5, 9], [5, 6, 10], [6, 0, 11], [0, 4, 3], [1, 5, 4], [2, 6, 5]]) == 75
    assert candidate(n = 6,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56
    assert candidate(n = 6,maxDistance = 4,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 0, 2], [0, 3, 1], [1, 4, 1], [2, 5, 1], [3, 0, 1], [4, 1, 1], [5, 2, 1]]) == 56
    assert candidate(n = 8,maxDistance = 25,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 0, 1], [7, 1, 1]]) == 208
    assert candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6], [0, 3, 2], [1, 4, 2], [2, 5, 2], [3, 0, 2], [4, 1, 2], [5, 2, 2]]) == 35
    assert candidate(n = 5,maxDistance = 3,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
    assert candidate(n = 10,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 1], [3, 7, 2], [4, 8, 5], [5, 9, 3], [6, 9, 6], [7, 8, 1], [8, 9, 2], [0, 3, 2], [1, 5, 1], [2, 4, 5]]) == 474
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 0, 3]]) == 19
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7], [0, 3, 8], [1, 4, 9], [2, 5, 10]]) == 24
    assert candidate(n = 7,maxDistance = 12,roads = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 4, 5], [3, 4, 2], [3, 5, 6], [4, 6, 3], [5, 6, 1]]) == 65
    assert candidate(n = 9,maxDistance = 25,roads = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 0, 11], [0, 4, 2], [1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 0, 7], [6, 1, 8], [7, 2, 9], [8, 3, 10]]) == 329
    assert candidate(n = 6,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]]) == 14
    assert candidate(n = 5,maxDistance = 20,roads = [[0, 1, 5], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]) == 22
    assert candidate(n = 5,maxDistance = 4,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 1], [3, 4, 2], [4, 0, 3]]) == 17
    assert candidate(n = 8,maxDistance = 12,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9]]) == 24
    assert candidate(n = 6,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 3], [4, 5, 4], [5, 0, 4]]) == 15
    assert candidate(n = 7,maxDistance = 8,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 0, 7], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 0, 5], [5, 1, 6], [6, 2, 7]]) == 71
    assert candidate(n = 5,maxDistance = 7,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 2, 2], [1, 3, 2], [2, 4, 2], [3, 0, 2], [4, 1, 2]]) == 32
    assert candidate(n = 8,maxDistance = 20,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 8], [0, 2, 2], [1, 3, 3], [2, 4, 4], [3, 5, 5], [4, 6, 6], [5, 7, 7]]) == 167
    assert candidate(n = 5,maxDistance = 7,roads = [[0, 1, 2], [1, 2, 2], [2, 3, 3], [3, 4, 1], [4, 0, 1]]) == 22
    assert candidate(n = 7,maxDistance = 15,roads = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [4, 5, 5], [5, 6, 5], [6, 4, 5], [4, 6, 3], [5, 4, 4]]) == 16
    assert candidate(n = 5,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 0, 6], [4, 1, 7]]) == 32
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 32
    assert candidate(n = 6,maxDistance = 7,roads = [[0, 1, 2], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 4, 2], [4, 5, 3]]) == 29
    assert candidate(n = 7,maxDistance = 8,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 5, 3], [5, 6, 3], [6, 0, 4]]) == 32
    assert candidate(n = 6,maxDistance = 9,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [0, 5, 6]]) == 21
    assert candidate(n = 5,maxDistance = 5,roads = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8], [3, 0, 9], [4, 1, 10]]) == 13
    assert candidate(n = 8,maxDistance = 15,roads = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 0, 9], [0, 5, 5], [1, 6, 6], [2, 7, 7], [3, 0, 0]]) == 115
    assert candidate(n = 5,maxDistance = 7,roads = [[0, 1, 3], [1, 2, 1], [2, 3, 2], [3, 4, 2], [4, 0, 5]]) == 18
    assert candidate(n = 6,maxDistance = 10,roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 0, 1], [5, 1, 1]]) == 61


