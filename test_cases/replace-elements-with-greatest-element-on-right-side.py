def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2]) == [2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2]) == [2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3]) == [3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3]) == [3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50]) == [50, 50, 50, 50, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50]) == [50, 50, 50, 50, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 40, 30, 20, 10]) == [40, 30, 20, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 40, 30, 20, 10]) == [40, 30, 20, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99999, 99998, 99997, 99996, 99995]) == [99998, 99997, 99996, 99995, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99999, 99998, 99997, 99996, 99995]) == [99998, 99997, 99996, 99995, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1]) == [1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1]) == [1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [400]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [400]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 100000, 100000]) == [100000, 100000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 100000, 100000]) == [100000, 100000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1]) == [3, 3, 3, 3, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1]) == [3, 3, 3, 3, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21]) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21]) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 100, 1000, 10000]) == [10000, 10000, 10000, 10000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 100, 1000, 10000]) == [10000, 10000, 10000, 10000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 50, 50, 50, 50, 50, 50, 50, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 50, 50, 50, 50, 50, 50, 50, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 3, 9, 1, 8, 5, 2]) == [9, 9, 9, 8, 8, 5, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 3, 9, 1, 8, 5, 2]) == [9, 9, 9, 8, 8, 5, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86]) == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86]) == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994]) == [99999, 99998, 99997, 99996, 99995, 99994, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994]) == [99999, 99998, 99997, 99996, 99995, 99994, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 9, 9, 9, 9, 6, 6, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 9, 9, 9, 9, 6, 6, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 3, 1, 3, 2, 3, 1, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 3, 1, 3, 2, 3, 1, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == [999, 998, 997, 996, 995, 994, 993, 992, 991, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == [999, 998, 997, 996, 995, 994, 993, 992, 991, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 9, 5, 5, 5, 5]) == [9, 9, 9, 9, 9, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 9, 5, 5, 5, 5]) == [9, 9, 9, 9, 9, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 2, 3, 1, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 2, 3, 1, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [45, 40, 35, 30, 25, 20, 15, 10, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [45, 40, 35, 30, 25, 20, 15, 10, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 4, 4, 4, 4, 4, 4, 4, 4, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 4, 4, 4, 4, 4, 4, 4, 4, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 3, 4, 2, 3, 1]) == [5, 5, 5, 5, 4, 4, 3, 3, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 3, 4, 2, 3, 1]) == [5, 5, 5, 5, 4, 4, 3, 3, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20]) == [20, 20, 20, 20, 20, 20, 20, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20]) == [20, 20, 20, 20, 20, 20, 20, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 3, 9, 2, 5, 6, 7, 8, 1]) == [9, 9, 9, 8, 8, 8, 8, 8, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 3, 9, 2, 5, 6, 7, 8, 1]) == [9, 9, 9, 8, 8, 8, 8, 8, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99, 9]) == [100000, 100000, 100000, 100000, 99999, 9999, 999, 99, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99, 9]) == [100000, 100000, 100000, 100000, 99999, 9999, 999, 99, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 1, 8, 9, 1, 4, 2, 10, 7]) == [10, 10, 10, 10, 10, 10, 10, 10, 7, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 1, 8, 9, 1, 4, 2, 10, 7]) == [10, 10, 10, 10, 10, 10, 10, 10, 7, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [60, 60, 60, 60, 60, 60, 60, 60, 60, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [60, 60, 60, 60, 60, 60, 60, 60, 60, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == [100000, 99999, 99999, 99998, 99998, 99997, 99997, 99996, 99996, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == [100000, 99999, 99999, 99998, 99998, 99997, 99997, 99996, 99996, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 6, 5, 4, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 6, 5, 4, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 3, 2, 7, 8, 5, 6]) == [8, 8, 8, 8, 8, 6, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 3, 2, 7, 8, 5, 6]) == [8, 8, 8, 8, 8, 6, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 3, 7, 2, 8, 6]) == [8, 8, 8, 8, 8, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 3, 7, 2, 8, 6]) == [8, 8, 8, 8, 8, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8]) == [8, 8, 8, 8, 8, 8, 8, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8]) == [8, 8, 8, 8, 8, 8, 8, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 100000, 100000, 100000]) == [100000, 100000, 100000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 100000, 100000, 100000]) == [100000, 100000, 100000, -1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1]
    assert candidate(arr = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, -1]
    assert candidate(arr = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, -1]
    assert candidate(arr = [1, 2]) == [2, -1]
    assert candidate(arr = [1, 2, 3]) == [3, 3, -1]
    assert candidate(arr = [17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert candidate(arr = [1]) == [-1]
    assert candidate(arr = [10, 20, 30, 40, 50]) == [50, 50, 50, 50, -1]
    assert candidate(arr = [50, 40, 30, 20, 10]) == [40, 30, 20, 10, -1]
    assert candidate(arr = [99999, 99998, 99997, 99996, 99995]) == [99998, 99997, 99996, 99995, -1]
    assert candidate(arr = [2, 1]) == [1, -1]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [400]) == [-1]
    assert candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, -1]
    assert candidate(arr = [100000, 100000, 100000]) == [100000, 100000, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, -1]
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995]) == [99999, 99998, 99997, 99996, 99995, -1]
    assert candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1]) == [3, 3, 3, 3, 3, 2, 1, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21]) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, -1]
    assert candidate(arr = [1, 10, 100, 1000, 10000]) == [10000, 10000, 10000, 10000, -1]
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]
    assert candidate(arr = [100000]) == [-1]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, -1, -1, -1, -1]
    assert candidate(arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, -1]
    assert candidate(arr = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 50, 50, 50, 50, 50, 50, 50, 5, -1]
    assert candidate(arr = [9, 4, 3, 9, 1, 8, 5, 2]) == [9, 9, 9, 8, 8, 5, 2, -1]
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 4, 3, 2, 1, -1]
    assert candidate(arr = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1]
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, -1]
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86]) == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, -1]
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, -1]
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994]) == [99999, 99998, 99997, 99996, 99995, 99994, -1]
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
    assert candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, -1]
    assert candidate(arr = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, -1]
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 9, 9, 9, 9, 6, 6, 5, 5, 5, -1]
    assert candidate(arr = [1, 3, 2, 3, 1, 3, 2, 3, 1, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
    assert candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
    assert candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == [999, 998, 997, 996, 995, 994, 993, 992, 991, -1]
    assert candidate(arr = [5, 5, 5, 5, 5, 9, 5, 5, 5, 5]) == [9, 9, 9, 9, 9, 5, 5, 5, 5, -1]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, -1]
    assert candidate(arr = [100, 90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
    assert candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, -1]
    assert candidate(arr = [3, 2, 2, 3, 1, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, -1]
    assert candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [45, 40, 35, 30, 25, 20, 15, 10, 5, -1]
    assert candidate(arr = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1]
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 4, 4, 4, 4, 4, 4, 4, 4, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
    assert candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, -1]
    assert candidate(arr = [1, 3, 2, 4, 5, 3, 4, 2, 3, 1]) == [5, 5, 5, 5, 4, 4, 3, 3, 1, -1]
    assert candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20]) == [20, 20, 20, 20, 20, 20, 20, -1]
    assert candidate(arr = [9, 4, 3, 9, 2, 5, 6, 7, 8, 1]) == [9, 9, 9, 8, 8, 8, 8, 8, 1, -1]
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99, 9]) == [100000, 100000, 100000, 100000, 99999, 9999, 999, 99, 9, -1]
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
    assert candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 1, -1]
    assert candidate(arr = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, -1]
    assert candidate(arr = [3, 5, 1, 8, 9, 1, 4, 2, 10, 7]) == [10, 10, 10, 10, 10, 10, 10, 10, 7, -1]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, -1]
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
    assert candidate(arr = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, -1]
    assert candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [60, 60, 60, 60, 60, 60, 60, 60, 60, -1]
    assert candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == [100000, 99999, 99999, 99998, 99998, 99997, 99997, 99996, 99996, -1]
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [1, 3, 2, 6, 5, 4, 7, 9, 8, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 2, -1]
    assert candidate(arr = [9, 4, 3, 2, 7, 8, 5, 6]) == [8, 8, 8, 8, 8, 6, 6, -1]
    assert candidate(arr = [9, 4, 3, 7, 2, 8, 6]) == [8, 8, 8, 8, 8, 6, -1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1]
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, -1]
    assert candidate(arr = [2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -1]
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, -1]
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, -1]
    assert candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8]) == [8, 8, 8, 8, 8, 8, 8, -1]
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, -1]
    assert candidate(arr = [100000, 100000, 100000, 100000]) == [100000, 100000, 100000, -1]


