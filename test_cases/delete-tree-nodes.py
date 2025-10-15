def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -5, 6, -6, 7, -7, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -5, 6, -6, 7, -7, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, -1, 1, -1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, -1, 1, -1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, 2, -3, 4, -4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, 2, -3, 4, -4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 1,parent = [-1],value = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 1,parent = [-1],value = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 3,parent = [-1, 0, 0],value = [1, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 3,parent = [-1, 0, 0],value = [1, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 4,parent = [-1, 0, 0, 1],value = [1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 4,parent = [-1, 0, 0, 1],value = [1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, 5, -10, 0, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, 5, -10, 0, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 1, -1, 0, 2, -2, 0, 3, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 1, -1, 0, 2, -2, 0, 3, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 4, 5, -3, -4, -5, -6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 4, 5, -3, -4, -5, -6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, -10, 1, 2, 3, 4, 1, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, -10, 1, 2, 3, 4, 1, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, -5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, -5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 4, -4, 5, -5, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 4, -4, 5, -5, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [10, -5, -5, 3, -3, 2, -2, 1, 1, 0, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [10, -5, -5, 3, -3, 2, -2, 1, 1, 0, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 5],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 5],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [10, -5, -5, 3, 3, -1, -1, 1, 1, 2, 2, 1, 1, -2, -2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [10, -5, -5, 3, 3, -1, -1, 1, 1, 2, 2, 1, 1, -2, -2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0, -6, 0, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0, -6, 0, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, -1, 2, -2, 3, -3, 4, -4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, -1, 2, -2, 3, -3, 4, -4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, 3, 0, -2, -3, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, 3, 0, -2, -3, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1, -1, -1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1, -1, -1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 4, -4, 5, -5, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 4, -4, 5, -5, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, -3, -2, 4, -4, 5, -5, 6, -6, 7]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, -3, -2, 4, -4, 5, -5, 6, -6, 7]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, 5, -6, 7, -8, 9, -10, 11, -12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, 5, -6, 7, -8, 9, -10, 11, -12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 1, -1, 1, -1, 1, -1, 1, -1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [5, 3, -2, 1, -1, 4, -4, 2, -2, -3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [5, 3, -2, 1, -1, 4, -4, 2, -2, -3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 0, 3, -2, 1, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 0, 3, -2, 1, -1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 4, 5, -4, -5, -3, -3, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 4, 5, -4, -5, -3, -3, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, 5, -6, -7, 8, 9, -10, -11, 12, -13, 14, -15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, 5, -6, -7, 8, 9, -10, -11, 12, -13, 14, -15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -100]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -100]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -100]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -100]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5],value = [5, -5, 3, -3, 2, -2, 4, -4, 1, -1, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5],value = [5, -5, 3, -3, 2, -2, 4, -4, 1, -1, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 1, 2, 3, -3, 4, -4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 1, 2, 3, -3, 4, -4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 0, -2, -3, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 0, -2, -3, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, -2, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, -2, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0]) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -5, 6, -6, 7, -7, 8]) == 10
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -2]) == 6
    assert candidate(nodes = 7,parent = [-1, 0, 0, 1, 2, 2, 2],value = [1, -2, 4, 0, -2, -1, -1]) == 2
    assert candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, -1, 1, -1, -1]) == 5
    assert candidate(nodes = 5,parent = [-1, 0, 0, 1, 1],value = [1, 2, -3, 4, -4]) == 0
    assert candidate(nodes = 1,parent = [-1],value = [0]) == 0
    assert candidate(nodes = 3,parent = [-1, 0, 0],value = [1, -1, 0]) == 0
    assert candidate(nodes = 4,parent = [-1, 0, 0, 1],value = [1, -1, 1, -1]) == 0
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, 5, -10, 0, -1, -1, -1, -1, -1]) == 0
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 1, -1, 0, 2, -2, 0, 3, -3]) == 0
    assert candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 9
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1]) == 5
    assert candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13]) == 25
    assert candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0]) == 1
    assert candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 0
    assert candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 4, 5, -3, -4, -5, -6]) == 4
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 15
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 4, -10, 1, 2, 3, 4, 1, 2, 3]) == 12
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 12
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, -5]) == 4
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
    assert candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 4, -4, 5, -5, 0]) == 0
    assert candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0]) == 4
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [10, -5, -5, 3, -3, 2, -2, 1, 1, 0, 0, 0]) == 9
    assert candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5]) == 1
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 5],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [10, -5, -5, 3, 3, -1, -1, 1, 1, 2, 2, 1, 1, -2, -2]) == 15
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 0, -2, -3, 0, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0, -6, 0, 7]) == 10
    assert candidate(nodes = 10,parent = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 0
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10
    assert candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, -1, 2, -2, 3, -3, 4, -4]) == 0
    assert candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 16
    assert candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, 3, 0, -2, -3, 0, 5]) == 5
    assert candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, -3, 4, -4, 5, -5, 0, 0, 0, 0]) == 0
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -10, 1, -1, -1, 1]) == 8
    assert candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0
    assert candidate(nodes = 10,parent = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7]) == 10
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 4, -4, 5, -5, 0, 0]) == 0
    assert candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 18
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, 3, -3, -2, 4, -4, 5, -5, 6, -6, 7]) == 12
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, 2, -3, 4, 5, -6, 7, -8, 9, -10, 11, -12]) == 0
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12]) == 20
    assert candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 0]) == 0
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -2, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
    assert candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
    assert candidate(nodes = 25,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 25
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [5, 3, -2, 1, -1, 4, -4, 2, -2, -3]) == 4
    assert candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 0]) == 0
    assert candidate(nodes = 8,parent = [-1, 0, 0, 1, 1, 2, 2, 3],value = [1, 2, -3, 0, 3, -2, 1, -1]) == 8
    assert candidate(nodes = 11,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],value = [1, 2, 3, 4, 5, -4, -5, -3, -3, 0, 0]) == 0
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3, 0, 1, 2, -3]) == 0
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7],value = [1, 2, -3, 4, 5, -6, -7, 8, 9, -10, -11, 12, -13, 14, -15]) == 15
    assert candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -100]) == 18
    assert candidate(nodes = 18,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18]) == 18
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],value = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 20
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0
    assert candidate(nodes = 14,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],value = [1, 2, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9]) == 14
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 0
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0]) == 0
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nodes = 13,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 0]) == 0
    assert candidate(nodes = 16,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -100]) == 16
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5],value = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0
    assert candidate(nodes = 12,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5],value = [5, -5, 3, -3, 2, -2, 4, -4, 1, -1, 0, 0]) == 0
    assert candidate(nodes = 10,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],value = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(nodes = 20,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],value = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == 20
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, -3, 1, 2, 3, -3, 4, -4]) == 9
    assert candidate(nodes = 9,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3],value = [1, 2, 3, 0, -2, -3, 0, 0, 0]) == 1
    assert candidate(nodes = 15,parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],value = [1, 2, -3, 0, -2, 4, 0, -4, 0, 5, 0, -5, 0, 6, 0]) == 11


