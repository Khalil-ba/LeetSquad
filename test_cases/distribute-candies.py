def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, 100000, -100000, -100000, 50000, 50000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, 100000, -100000, -100000, 50000, 50000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -2, -3, -1, -2, -3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -2, -3, -1, -2, -3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -1, 0, 0, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -1, 0, 0, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, -100000, 100000, -100000, 100000, -100000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, -100000, 100000, -100000, 100000, -100000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -2, -3, -4, -5, -6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -2, -3, -4, -5, -6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, -100000, 100000, -100000, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, -100000, 100000, -100000, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [6, 6, 6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [6, 6, 6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -2, -2, -3, -3, -4, -4, -4, -5, -5, -5, -5, -6, -6, -7, -7, -7, -7, -8, -8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -2, -2, -3, -3, -4, -4, -4, -5, -5, -5, -5, -6, -6, -7, -7, -7, -7, -8, -8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, 50000, -49999, 49999, -49998, 49998, -49997, 49997, -49996, 49996, -49995, 49995, -49994, 49994, -49993, 49993, -49992, 49992, -49991, 49991]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, 50000, -49999, 49999, -49998, 49998, -49997, 49997, -49996, 49996, -49995, 49995, -49994, 49994, -49993, 49993, -49992, 49992, -49991, 49991]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, -49999, -49998, -49997, -49996, -49995, -49994, -49993, -49992, -49991, 50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, -49999, -49998, -49997, -49996, -49995, -49994, -49993, -49992, -49991, 50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, 50000, -40000, 40000, -30000, 30000, -20000, 20000, -10000, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, 50000, -40000, 40000, -30000, 30000, -20000, 20000, -10000, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, -49999, -49998, -49997, 49998, 49999, 50000, 50001, 50002, 50003]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, -49999, -49998, -49997, 49998, 49999, 50000, 50001, 50002, 50003]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10000, 20000, 30000, 40000, 50000, 10000, 20000, 30000, 40000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10000, 20000, 30000, 40000, 50000, 10000, 20000, 30000, 40000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10, -11, -11, -12, -12, -13, -13, -14, -15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10, -11, -11, -12, -12, -13, -13, -14, -15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, -99969, -99968, -99967, -99966, -99965]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, -99969, -99968, -99967, -99966, -99965]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [-50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [-50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50, 60, 60, 60, 60, 70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50, 60, 60, 60, 60, 70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [10000, 10000, 9999, 9999, 8888, 8888, 7777, 7777, 6666, 6666, 5555, 5555, 4444, 4444, 3333, 3333, 2222, 2222, 1111, 1111]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [10000, 10000, 9999, 9999, 8888, 8888, 7777, 7777, 6666, 6666, 5555, 5555, 4444, 4444, 3333, 3333, 2222, 2222, 1111, 1111]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(candyType = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]) == 3
    assert candidate(candyType = [1, 1, 2, 3]) == 2
    assert candidate(candyType = [1, 1, 1, 2, 2, 2]) == 2
    assert candidate(candyType = [0, 0, 0, 0, 0, 0]) == 1
    assert candidate(candyType = [100000, 100000, -100000, -100000, 50000, 50000]) == 3
    assert candidate(candyType = [-1, -2, -3, -1, -2, -3]) == 3
    assert candidate(candyType = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    assert candidate(candyType = [1, 2, 3, 1, 2, 3]) == 3
    assert candidate(candyType = [-1, -1, 0, 0, 1, 1]) == 3
    assert candidate(candyType = [100000, -100000, 100000, -100000, 100000, -100000]) == 2
    assert candidate(candyType = [1, 2, 3, 4]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6]) == 3
    assert candidate(candyType = [1, 2, 1, 2, 1, 2]) == 2
    assert candidate(candyType = [-1, -2, -3, -4, -5, -6]) == 3
    assert candidate(candyType = [1, 1, 2, 2, 3, 3]) == 3
    assert candidate(candyType = [100000, -100000, 100000, -100000, 0, 0]) == 3
    assert candidate(candyType = [6, 6, 6, 6]) == 1
    assert candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2]) == 2
    assert candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]) == 4
    assert candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]) == 11
    assert candidate(candyType = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2]) == 20
    assert candidate(candyType = [-1, -2, -2, -3, -3, -4, -4, -4, -5, -5, -5, -5, -6, -6, -7, -7, -7, -7, -8, -8]) == 8
    assert candidate(candyType = [-100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
    assert candidate(candyType = [-50000, 50000, -49999, 49999, -49998, 49998, -49997, 49997, -49996, 49996, -49995, 49995, -49994, 49994, -49993, 49993, -49992, 49992, -49991, 49991]) == 10
    assert candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4]) == 4
    assert candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 10
    assert candidate(candyType = [-50000, -49999, -49998, -49997, -49996, -49995, -49994, -49993, -49992, -49991, 50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991]) == 10
    assert candidate(candyType = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(candyType = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18]) == 18
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [-50000, 50000, -40000, 40000, -30000, 30000, -20000, 20000, -10000, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]) == 11
    assert candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(candyType = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000]) == 2
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19
    assert candidate(candyType = [-50000, -49999, -49998, -49997, 49998, 49999, 50000, 50001, 50002, 50003]) == 5
    assert candidate(candyType = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 15
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50]) == 5
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]) == 10
    assert candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 19
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]) == 4
    assert candidate(candyType = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == 5
    assert candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(candyType = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 25
    assert candidate(candyType = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(candyType = [10000, 20000, 30000, 40000, 50000, 10000, 20000, 30000, 40000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15
    assert candidate(candyType = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]) == 4
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == 16
    assert candidate(candyType = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000]) == 10
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 20
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20]) == 18
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 30
    assert candidate(candyType = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 4
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16
    assert candidate(candyType = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]) == 7
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 4
    assert candidate(candyType = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10, -11, -11, -12, -12, -13, -13, -14, -15]) == 14
    assert candidate(candyType = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15
    assert candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 5
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20
    assert candidate(candyType = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
    assert candidate(candyType = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, -99969, -99968, -99967, -99966, -99965]) == 18
    assert candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8
    assert candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15]) == 14
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(candyType = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6
    assert candidate(candyType = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 15
    assert candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8]) == 8
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(candyType = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15]) == 15
    assert candidate(candyType = [-50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, -50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 20
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(candyType = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50, 60, 60, 60, 60, 70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90]) == 9
    assert candidate(candyType = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 14
    assert candidate(candyType = [10000, 10000, 9999, 9999, 8888, 8888, 7777, 7777, 6666, 6666, 5555, 5555, 4444, 4444, 3333, 3333, 2222, 2222, 1111, 1111]) == 10
    assert candidate(candyType = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(candyType = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
    assert candidate(candyType = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 8
    assert candidate(candyType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(candyType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3


