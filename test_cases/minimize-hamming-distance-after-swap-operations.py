def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 2], [1, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 2], [1, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1],target = [1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1],target = [1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4],target = [1, 3, 2, 4],allowedSwaps = []) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4],target = [1, 3, 2, 4],allowedSwaps = []) == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4],target = [2, 1, 4, 5],allowedSwaps = [[0, 1], [2, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4],target = [2, 1, 4, 5],allowedSwaps = [[0, 1], [2, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(source = [5, 1, 2, 4, 3],target = [1, 5, 4, 2, 3],allowedSwaps = [[0, 4], [4, 2], [1, 3], [1, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [5, 1, 2, 4, 3],target = [1, 5, 4, 2, 3],allowedSwaps = [[0, 4], [4, 2], [1, 3], [1, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [4, 5, 6],target = [6, 4, 5],allowedSwaps = [[0, 1], [1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 5, 6],target = [6, 4, 5],allowedSwaps = [[0, 1], [1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30],target = [30, 20, 10],allowedSwaps = [[0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30],target = [30, 20, 10],allowedSwaps = [[0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1],target = [2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1],target = [2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 2, 1],target = [2, 1, 1, 2],allowedSwaps = [[0, 1], [2, 3], [1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 2, 1],target = [2, 1, 1, 2],allowedSwaps = [[0, 1], [2, 3], [1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9],target = [9, 7, 5, 3, 1],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9],target = [9, 7, 5, 3, 1],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 2, 1, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4], [0, 1], [2, 3], [4, 5], [6, 7]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 2, 1, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4], [0, 1], [2, 3], [4, 5], [6, 7]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],allowedSwaps = [[0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],allowedSwaps = [[0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],target = [5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1],allowedSwaps = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],target = [5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1],allowedSwaps = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [3, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [3, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 3], [3, 2], [4, 1], [5, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 3], [3, 2], [4, 1], [5, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],target = [99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],target = [99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9, 11],target = [11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9, 11],target = [11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9, 11, 13, 15],target = [15, 13, 11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 7], [1, 6], [2, 5], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9, 11, 13, 15],target = [15, 13, 11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 7], [1, 6], [2, 5], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = [90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = [90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = []) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = []) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],target = [8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],target = [8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 4], [1, 3], [2, 8], [5, 7], [6, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 4], [1, 3], [2, 8], [5, 7], [6, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 20, 50, 40, 30, 10],allowedSwaps = [[0, 5], [2, 4], [0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 20, 50, 40, 30, 10],allowedSwaps = [[0, 5], [2, 4], [0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],allowedSwaps = []) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],allowedSwaps = []) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [0, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [0, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = []) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = []) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 2, 2, 3, 3],target = [3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 2], [0, 4], [1, 3], [1, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 2, 2, 3, 3],target = [3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 2], [0, 4], [1, 3], [1, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7], [0, 8], [1, 9], [2, 5], [3, 6], [4, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7], [0, 8], [1, 9], [2, 5], [3, 6], [4, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1], [1, 9], [9, 8]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1], [1, 9], [9, 8]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [3, 2, 1, 4, 5],target = [5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [3, 2, 1, 4, 5],target = [5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [4, 1, 3, 2],target = [2, 3, 1, 4],allowedSwaps = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 1, 3, 2],target = [2, 3, 1, 4],allowedSwaps = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],target = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],target = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = [7, 8, 9, 10, 11, 12],target = [10, 11, 12, 7, 8, 9],allowedSwaps = [[0, 3], [1, 4], [2, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [7, 8, 9, 10, 11, 12],target = [10, 11, 12, 7, 8, 9],allowedSwaps = [[0, 3], [1, 4], [2, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 1, 2, 2, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 1, 2, 2, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],target = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],target = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [100000, 90000, 80000, 70000],target = [70000, 80000, 90000, 100000],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [100000, 90000, 80000, 70000],target = [70000, 80000, 90000, 100000],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [4, 4, 4, 4, 4],target = [1, 2, 3, 4, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [4, 4, 4, 4, 4],target = [1, 2, 3, 4, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 2, 9, 3, 8, 4, 7, 5, 6, 1],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 2, 9, 3, 8, 4, 7, 5, 6, 1],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],target = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 8], [5, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],target = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 8], [5, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = []) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = []) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0
    assert candidate(source = [4, 3, 2, 1],target = [1, 2, 3, 4],allowedSwaps = [[0, 2], [1, 3]]) == 4
    assert candidate(source = [1, 1, 1, 1],target = [1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 0
    assert candidate(source = [1, 2, 3, 4],target = [1, 3, 2, 4],allowedSwaps = []) == 2
    assert candidate(source = [1, 2, 3, 4],target = [2, 1, 4, 5],allowedSwaps = [[0, 1], [2, 3]]) == 1
    assert candidate(source = [5, 1, 2, 4, 3],target = [1, 5, 4, 2, 3],allowedSwaps = [[0, 4], [4, 2], [1, 3], [1, 4]]) == 0
    assert candidate(source = [4, 5, 6],target = [6, 4, 5],allowedSwaps = [[0, 1], [1, 2]]) == 0
    assert candidate(source = [10, 20, 30],target = [30, 20, 10],allowedSwaps = [[0, 2]]) == 0
    assert candidate(source = [1, 1, 1, 1],target = [2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3]]) == 4
    assert candidate(source = [1, 2, 2, 1],target = [2, 1, 1, 2],allowedSwaps = [[0, 1], [2, 3], [1, 2]]) == 0
    assert candidate(source = [1, 3, 5, 7, 9],target = [9, 7, 5, 3, 1],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0
    assert candidate(source = [1, 2, 2, 1, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4], [0, 1], [2, 3], [4, 5], [6, 7]]) == 2
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],allowedSwaps = [[0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9]]) == 4
    assert candidate(source = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],target = [5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1],allowedSwaps = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 8
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
    assert candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [3, 3]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 3], [3, 2], [4, 1], [5, 0]]) == 0
    assert candidate(source = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],target = [99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 0
    assert candidate(source = [7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
    assert candidate(source = [1, 3, 5, 7, 9, 11],target = [11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
    assert candidate(source = [1, 3, 5, 7, 9, 11, 13, 15],target = [15, 13, 11, 9, 7, 5, 3, 1],allowedSwaps = [[0, 7], [1, 6], [2, 5], [3, 4]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = [90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 0
    assert candidate(source = [5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = []) == 10
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6]]) == 0
    assert candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],target = [8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1]]) == 9
    assert candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 4], [1, 3], [2, 8], [5, 7], [6, 9]]) == 8
    assert candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7]]) == 8
    assert candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 20, 50, 40, 30, 10],allowedSwaps = [[0, 5], [2, 4], [0, 2]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3], [2, 2]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 6
    assert candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],allowedSwaps = []) == 0
    assert candidate(source = [7, 8, 9, 10, 11, 12, 13],target = [13, 12, 11, 10, 9, 8, 7],allowedSwaps = [[0, 6], [1, 5], [2, 4], [0, 3]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50],target = [50, 40, 30, 20, 10],allowedSwaps = [[0, 4], [1, 3]]) == 0
    assert candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = []) == 10
    assert candidate(source = [1, 1, 2, 2, 3, 3],target = [3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 2], [0, 4], [1, 3], [1, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 20
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == 0
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10
    assert candidate(source = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7], [0, 8], [1, 9], [2, 5], [3, 6], [4, 7]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],allowedSwaps = [[0, 1], [1, 9], [9, 8]]) == 7
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0
    assert candidate(source = [3, 2, 1, 4, 5],target = [5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 16
    assert candidate(source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(source = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [4, 1, 3, 2],target = [2, 3, 1, 4],allowedSwaps = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3]]) == 0
    assert candidate(source = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 6], [7, 8]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == 0
    assert candidate(source = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],target = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 12
    assert candidate(source = [7, 8, 9, 10, 11, 12],target = [10, 11, 12, 7, 8, 9],allowedSwaps = [[0, 3], [1, 4], [2, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 10
    assert candidate(source = [1, 1, 1, 1, 1],target = [1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [1, 5], [2, 6], [3, 7]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]) == 0
    assert candidate(source = [10, 20, 30, 40, 50, 60],target = [60, 50, 40, 30, 20, 10],allowedSwaps = [[0, 5], [1, 4], [2, 3]]) == 0
    assert candidate(source = [1, 1, 2, 2, 3, 3, 4, 4],target = [4, 4, 3, 3, 2, 2, 1, 1],allowedSwaps = [[0, 6], [1, 7], [2, 5], [3, 4]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = [9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 8], [1, 7], [2, 6], [3, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],target = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == 0
    assert candidate(source = [100000, 90000, 80000, 70000],target = [70000, 80000, 90000, 100000],allowedSwaps = [[0, 3], [1, 2], [0, 1], [2, 3]]) == 0
    assert candidate(source = [4, 4, 4, 4, 4],target = [1, 2, 3, 4, 5],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 4
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],allowedSwaps = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [10, 2, 9, 3, 8, 4, 7, 5, 6, 1],allowedSwaps = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 5
    assert candidate(source = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 10
    assert candidate(source = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],target = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],allowedSwaps = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 3], [4, 8], [5, 7]]) == 0
    assert candidate(source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],allowedSwaps = []) == 0
    assert candidate(source = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],allowedSwaps = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10


