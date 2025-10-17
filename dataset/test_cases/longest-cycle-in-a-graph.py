def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(edges = [-1, 2, 0, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [-1, 2, 0, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 4, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 4, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 5, 4, 5, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 5, 4, 5, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 1, -1, -1, -1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 1, -1, -1, -1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [0, 1, 2, 3, 4, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [0, 1, 2, 3, 4, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 1, 3, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 1, 3, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 1, 4, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 1, 4, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [-1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [-1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [0, 1, 2, 3, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [0, 1, 2, 3, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 3, 2, 1, 0, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 3, 2, 1, 0, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 4, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 4, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 4, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 4, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [0, 1, 2, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [0, 1, 2, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 2, 0, 5, 6, 7, 8, 9, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 2, 0, 5, 6, 7, 8, 9, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 3, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 3, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 5, 6, 7, 8, 9, 3, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 5, 6, 7, 8, 9, 3, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 4, -1, 5, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 4, -1, 5, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 4, 2, 3, 5, 5, 6, 7, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 4, 2, 3, 5, 5, 6, 7, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 2, 0, 1, -1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 2, 0, 1, -1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1, 1, -1, -1, -1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1, 1, -1, -1, -1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 5, 6, 3, 4, 8, -1, 9, 10, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 5, 6, 3, 4, 8, -1, 9, 10, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 3, 2, -1, -1, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 3, 2, -1, -1, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11, 21, 22, 23, 24, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11, 21, 22, 23, 24, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 0, 5, 5, 5, 0, 7, 7, 7, 0, 9, 9, 9, 0, 11, 11, 11, 0, 13, 13, 13, 0, 15, 15, 15, 0, 17, 17, 17, 0, 19, 19, 19, 0, 21, 21, 21, 0, 23, 23, 23, 0, 25, 25, 25, 0, 27, 27, 27, 0, 29, 29, 29, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 0, 5, 5, 5, 0, 7, 7, 7, 0, 9, 9, 9, 0, 11, 11, 11, 0, 13, 13, 13, 0, 15, 15, 15, 0, 17, 17, 17, 0, 19, 19, 19, 0, 21, 21, 21, 0, 23, 23, 23, 0, 25, 25, 25, 0, 27, 27, 27, 0, 29, 29, 29, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 12, 14, 15, 16, 17, 18, 19, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 12, 14, 15, 16, 17, 18, 19, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(edges = [7, 4, 5, 6, 3, 1, 2, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [7, 4, 5, 6, 3, 1, 2, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 2, 0, 1, 2, -1, -1, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 2, 0, 1, 2, -1, -1, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 4, 5, 0, -1, -1, -1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 4, 5, 0, -1, -1, -1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 4, 2, 3, -1, 5, 5, 6, 7, -1, 8, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1, 17, 18, -1, 19, 20, -1, 21, 22, -1, 23, 24, -1, 25, 26, -1, 27, 28, -1, 29, 30, -1, 31, 32, -1, 33, 34, -1, 35, 36, -1, 37, 38, -1, 39, 40, -1, 41, 42, -1, 43, 44, -1, 45, 46, -1, 47, 48, -1, 49, 50, -1, 51, 52, -1, 53, 54, -1, 55, 56, -1, 57, 58, -1, 59, 60, -1, 61, 62, -1, 63, 64, -1, 65, 66, -1, 67, 68, -1, 69, 70, -1, 71, 72, -1, 73, 74, -1, 75, 76, -1, 77, 78, -1, 79, 80, -1, 81, 82, -1, 83, 84, -1, 85, 86, -1, 87, 88, -1, 89, 90, -1, 91, 92, -1, 93, 94, -1, 95, 96, -1, 97, 98, -1, 99, 100, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 4, 2, 3, -1, 5, 5, 6, 7, -1, 8, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1, 17, 18, -1, 19, 20, -1, 21, 22, -1, 23, 24, -1, 25, 26, -1, 27, 28, -1, 29, 30, -1, 31, 32, -1, 33, 34, -1, 35, 36, -1, 37, 38, -1, 39, 40, -1, 41, 42, -1, 43, 44, -1, 45, 46, -1, 47, 48, -1, 49, 50, -1, 51, 52, -1, 53, 54, -1, 55, 56, -1, 57, 58, -1, 59, 60, -1, 61, 62, -1, 63, 64, -1, 65, 66, -1, 67, 68, -1, 69, 70, -1, 71, 72, -1, 73, 74, -1, 75, 76, -1, 77, 78, -1, 79, 80, -1, 81, 82, -1, 83, 84, -1, 85, 86, -1, 87, 88, -1, 89, 90, -1, 91, 92, -1, 93, 94, -1, 95, 96, -1, 97, 98, -1, 99, 100, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 3, 2, 2, 0, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 3, 2, 2, 0, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 3, 4, 5, -1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 3, 4, 5, -1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 4, -1, 5, 6, 7, 8, -1, 9, 10, 11, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 4, -1, 5, 6, 7, 8, -1, 9, 10, 11, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 4, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 4, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 3, 4, 2, 1, -1, -1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 3, 4, 2, 1, -1, -1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(edges = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 4, 2, 3, 5, -1, 6, 7, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 4, 2, 3, 5, -1, 6, 7, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 4, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 4, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 3, 2, 1, -1, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 3, 2, 1, -1, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 0]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 0]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(edges = [9, 9, 9, 9, 9, 9, 9, 9, 9, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [9, 9, 9, 9, 9, 9, 9, 9, 9, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1, -1, 5, 6, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1, -1, 5, 6, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 4, 2, 3, 3, 4, 2, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 4, 2, 3, 3, 4, 2, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 5, 5, 5, 5, -1, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 5, 5, 5, 5, -1, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 5, 4, 3, -1, -1, 6, 8, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 5, 4, 3, -1, -1, 6, 8, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 4, 5, 5, 3, -1, 6, 7, 8, 9, 10, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 4, 5, 5, 3, -1, 6, 7, 8, 9, 10, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 4, 5, -1, 6, 7, 5, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 4, 5, -1, 6, 7, 5, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 2, 0, 4, 2, 2, 0, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 2, 0, 4, 2, 2, 0, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(edges = [-1, 3, -1, -1, 5, -1, 7, -1, 9, -1, 11, -1, 13, -1, 15, -1, 17, -1, 19, -1, 21, -1, 23, -1, 25, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [-1, 3, -1, -1, 5, -1, 7, -1, 9, -1, 11, -1, 13, -1, 15, -1, 17, -1, 19, -1, 21, -1, 23, -1, 25, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, -1, 10, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, -1, 10, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 3, 0, 5, 3, -1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 3, 0, 5, 3, -1, 2]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(edges = [-1, 2, 0, 1, -1]) == -1
    assert candidate(edges = [1, 2, 0, 4, -1]) == 3
    assert candidate(edges = [5, 4, 5, 4, 5, 4]) == 2
    assert candidate(edges = [1, 0, -1, -1]) == 2
    assert candidate(edges = [1, 1, 1, 1, 1]) == 1
    assert candidate(edges = [1, 0, 0, 0, 1]) == 2
    assert candidate(edges = [1, 0, -1, -1, -1]) == 2
    assert candidate(edges = [2, -1, 1, -1, -1, -1, -1, -1, -1, -1]) == -1
    assert candidate(edges = [1, 1, 1, 1, 1, 0]) == 1
    assert candidate(edges = [5, 4, 3, 2, 1, 0]) == 2
    assert candidate(edges = [0, 1, 2, 3, 4, -1]) == 1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
    assert candidate(edges = [1, 2, 0, 1, 3, -1]) == 3
    assert candidate(edges = [1, 2, 0, -1]) == 3
    assert candidate(edges = [1, 2, 3, 4, 0]) == 5
    assert candidate(edges = [3, 0, 1, 4, 2]) == 5
    assert candidate(edges = [-1, -1, -1, -1, -1]) == -1
    assert candidate(edges = [0, 1, 2, 3, -1]) == 1
    assert candidate(edges = [5, 4, 3, 2, 1, 0, -1, -1, -1, -1]) == 2
    assert candidate(edges = [3, 3, 4, 2, 3]) == 3
    assert candidate(edges = [1, 1, 1, 1, 1, 1]) == 1
    assert candidate(edges = [2, -1, 3, 1]) == -1
    assert candidate(edges = [4, 4, 4, 4, 4]) == 1
    assert candidate(edges = [1, 0, 0, 0, 0]) == 2
    assert candidate(edges = [0, 1, 2, -1, -1]) == 1
    assert candidate(edges = [1, 2, 3, 4, 5, 0]) == 6
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11]) == 10
    assert candidate(edges = [3, 1, 2, 0, 5, 6, 7, 8, 9, 4]) == 6
    assert candidate(edges = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9, -1]) == 3
    assert candidate(edges = [1, 3, 2, 3]) == 1
    assert candidate(edges = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 1
    assert candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(edges = [1, 2, 0, 5, 6, 7, 8, 9, 3, 4]) == 7
    assert candidate(edges = [2, 3, 4, -1, 5, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1
    assert candidate(edges = [3, 3, 4, 2, 3, 5, 5, 6, 7, 7]) == 3
    assert candidate(edges = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2
    assert candidate(edges = [5, 4, 0, 2, 0, 1, -1, 3]) == 4
    assert candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
    assert candidate(edges = [1, 2, 0, -1, 1, -1, -1, -1, -1, -1]) == 3
    assert candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 10]) == 10
    assert candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(edges = [1, 2, 0, 5, 6, 3, 4, 8, -1, 9, 10, -1]) == 3
    assert candidate(edges = [2, 2, 3, 2, 2]) == 2
    assert candidate(edges = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(edges = [1, 0, 3, 2, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(edges = [2, 1, 2]) == 1
    assert candidate(edges = [3, 3, 3, 1, 2]) == 2
    assert candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11, 21, 22, 23, 24, 20]) == 10
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1
    assert candidate(edges = [3, 3, 3, 0, 5, 5, 5, 0, 7, 7, 7, 0, 9, 9, 9, 0, 11, 11, 11, 0, 13, 13, 13, 0, 15, 15, 15, 0, 17, 17, 17, 0, 19, 19, 19, 0, 21, 21, 21, 0, 23, 23, 23, 0, 25, 25, 25, 0, 27, 27, 27, 0, 29, 29, 29, 0]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 12, 14, 15, 16, 17, 18, 19, -1]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0]) == 41
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30]) == 10
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 0]) == 8
    assert candidate(edges = [7, 4, 5, 6, 3, 1, 2, 0]) == 6
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 31
    assert candidate(edges = [5, 4, 0, 2, 0, 1, 2, -1, -1, 10, 9]) == 4
    assert candidate(edges = [2, 3, 4, 5, 0, -1, -1, -1, -1, -1]) == 3
    assert candidate(edges = [3, 3, 4, 2, 3, -1, 5, 5, 6, 7, -1, 8, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1, 17, 18, -1, 19, 20, -1, 21, 22, -1, 23, 24, -1, 25, 26, -1, 27, 28, -1, 29, 30, -1, 31, 32, -1, 33, 34, -1, 35, 36, -1, 37, 38, -1, 39, 40, -1, 41, 42, -1, 43, 44, -1, 45, 46, -1, 47, 48, -1, 49, 50, -1, 51, 52, -1, 53, 54, -1, 55, 56, -1, 57, 58, -1, 59, 60, -1, 61, 62, -1, 63, 64, -1, 65, 66, -1, 67, 68, -1, 69, 70, -1, 71, 72, -1, 73, 74, -1, 75, 76, -1, 77, 78, -1, 79, 80, -1, 81, 82, -1, 83, 84, -1, 85, 86, -1, 87, 88, -1, 89, 90, -1, 91, 92, -1, 93, 94, -1, 95, 96, -1, 97, 98, -1, 99, 100, -1]) == 3
    assert candidate(edges = [1, 3, 2, 2, 0, -1, -1, -1, -1, -1]) == 1
    assert candidate(edges = [1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3]) == 1
    assert candidate(edges = [1, 2, 0, 3, 4, 5, -1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 3
    assert candidate(edges = [2, 3, 4, -1, 5, 6, 7, 8, -1, 9, 10, 11, -1]) == 1
    assert candidate(edges = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(edges = [1, 2, 0, 4, 3]) == 3
    assert candidate(edges = [1, 3, 4, 2, 1, -1, -1, -1]) == 4
    assert candidate(edges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 1]) == 6
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0]) == 100
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 20
    assert candidate(edges = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 11
    assert candidate(edges = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 16
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4]) == 21
    assert candidate(edges = [3, 3, 4, 2, 3, 5, -1, 6, 7, 5]) == 3
    assert candidate(edges = [4, 4, 4, 4, 0]) == 2
    assert candidate(edges = [5, 4, 3, 2, 1, -1, -1, -1, -1, -1]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 0]) == 201
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 20
    assert candidate(edges = [9, 9, 9, 9, 9, 9, 9, 9, 9, 0]) == 2
    assert candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(edges = [1, 2, 0, -1, -1, 5, 6, 5]) == 3
    assert candidate(edges = [3, 3, 4, 2, 3, 3, 4, 2, 3, 3]) == 3
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]) == 10
    assert candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]) == 5
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]) == 15
    assert candidate(edges = [3, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(edges = [5, 5, 5, 5, 5, -1, 5, 5, 5, 5]) == -1
    assert candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5
    assert candidate(edges = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, -1]) == 1
    assert candidate(edges = [1, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 5]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0]) == 30
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 50
    assert candidate(edges = [1, 2, 0, 5, 4, 3, -1, -1, 6, 8, 7]) == 3
    assert candidate(edges = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]) == 5
    assert candidate(edges = [3, 4, 5, 5, 3, -1, 6, 7, 8, 9, 10, -1]) == 1
    assert candidate(edges = [1, 2, 0, 4, 5, -1, 6, 7, 5, 8]) == 3
    assert candidate(edges = [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0]) == 2
    assert candidate(edges = [5, 4, 0, 2, 0, 4, 2, 2, 0, 4]) == 3
    assert candidate(edges = [5, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, -1]) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0]) == 40
    assert candidate(edges = [-1, 3, -1, -1, 5, -1, 7, -1, 9, -1, 11, -1, 13, -1, 15, -1, 17, -1, 19, -1, 21, -1, 23, -1, 25, -1]) == -1
    assert candidate(edges = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3
    assert candidate(edges = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, -1, 10, -1]) == 1
    assert candidate(edges = [4, 3, 0, 5, 3, -1, 2]) == -1


