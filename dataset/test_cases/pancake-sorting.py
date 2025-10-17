def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 3, 4, 5]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 3, 4, 5]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 3, 2, 1]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 3, 2, 1]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2]) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2]) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 3, 4, 2]) == [2, 5, 2, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 3, 4, 2]) == [2, 5, 2, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 1, 5]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 1, 5]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3]) == []: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 4, 3, 2]) == [2, 5, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 4, 3, 2]) == [2, 5, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 4, 1]) == [3, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 4, 1]) == [3, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2]) == [2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2]) == [2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 5, 1, 2, 4]) == [6, 4, 5, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 5, 1, 2, 4]) == [6, 4, 5, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 1, 3, 4]) == [2, 5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 1, 3, 4]) == [2, 5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [11, 10, 5, 9, 8, 7, 2, 6, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [11, 10, 5, 9, 8, 7, 2, 6, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 2, 6, 5]) == [5, 6, 5, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 2, 6, 5]) == [5, 6, 5, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 2, 6, 4, 5, 3]) == [7, 4, 6, 4, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 2, 6, 4, 5, 3]) == [7, 4, 6, 4, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 3, 5, 7, 9, 2, 4, 8, 6]) == [2, 10, 5, 9, 6, 8, 6, 7, 6, 5, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 3, 5, 7, 9, 2, 4, 8, 6]) == [2, 10, 5, 9, 6, 8, 6, 7, 6, 5, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 1, 3]) == [2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 1, 3]) == [2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 8, 2, 9, 3, 10, 4, 5, 6]) == [7, 10, 8, 9, 7, 8, 6, 7, 4, 6, 2, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 8, 2, 9, 3, 10, 4, 5, 6]) == [7, 10, 8, 9, 7, 8, 6, 7, 4, 6, 2, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 5, 10, 9, 3, 7, 6, 4, 2, 1]) == [3, 10, 7, 9, 2, 8, 2, 7, 5, 6, 2, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 5, 10, 9, 3, 7, 6, 4, 2, 1]) == [3, 10, 7, 9, 2, 8, 2, 7, 5, 6, 2, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 8, 9, 7, 8, 6, 7, 5, 6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 8, 9, 7, 8, 6, 7, 5, 6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]) == [9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]) == [9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 5, 3, 1, 2, 4]) == [6, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 5, 3, 1, 2, 4]) == [6, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 4, 3, 6, 5]) == [5, 6, 5, 2, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 4, 3, 6, 5]) == [5, 6, 5, 2, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 2]) == [3, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 2]) == [3, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 6, 4, 2, 1, 3, 5, 7]) == [8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 6, 4, 2, 1, 3, 5, 7]) == [8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 6, 7, 5, 3, 1, 4, 9, 2, 10]) == [8, 9, 2, 8, 5, 7, 2, 6, 5, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 6, 7, 5, 3, 1, 4, 9, 2, 10]) == [8, 9, 2, 8, 5, 7, 2, 6, 5, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]) == [6, 10, 4, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]) == [6, 10, 4, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 10, 4, 8, 5, 9, 1, 6, 2, 3]) == [2, 10, 5, 9, 3, 8, 6, 7, 3, 6, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 10, 4, 8, 5, 9, 1, 6, 2, 3]) == [2, 10, 5, 9, 3, 8, 6, 7, 3, 6, 5, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 2, 3]) == [5, 3, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 2, 3]) == [5, 3, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 1, 4, 2]) == [5, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 1, 4, 2]) == [5, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == [10, 2, 9, 6, 7, 6, 2, 5, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == [10, 2, 9, 6, 7, 6, 2, 5, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 5, 9, 1, 7, 3, 4, 2, 6]) == [3, 9, 7, 8, 6, 7, 3, 6, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 5, 9, 1, 7, 3, 4, 2, 6]) == [3, 9, 7, 8, 6, 7, 3, 6, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 2, 3, 1]) == [5, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 2, 3, 1]) == [5, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 6, 2, 5, 3, 4]) == [7, 5, 6, 4, 5, 3, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 6, 2, 5, 3, 4]) == [7, 5, 6, 4, 5, 3, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 6, 3, 5, 2, 1]) == [2, 6, 3, 5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 6, 3, 5, 2, 1]) == [2, 6, 3, 5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 4, 2, 1, 3, 5]) == [6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 4, 2, 1, 3, 5]) == [6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 7, 4, 1, 8, 3, 6, 5]) == [5, 8, 5, 7, 4, 6, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 7, 4, 1, 8, 3, 6, 5]) == [5, 8, 5, 7, 4, 6, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 1, 7, 5, 4, 2]) == [4, 7, 5, 6, 4, 5, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 1, 7, 5, 4, 2]) == [4, 7, 5, 6, 4, 5, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 1, 5, 2, 4, 3]) == [6, 4, 5, 3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 1, 5, 2, 4, 3]) == [6, 4, 5, 3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 3, 2, 5, 6, 7, 8, 9, 10]) == [2, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 3, 2, 5, 6, 7, 8, 9, 10]) == [2, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == [3, 8, 3, 7, 3, 6, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == [3, 8, 3, 7, 3, 6, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4]) == [4, 5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4]) == [4, 5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 6, 5]) == [5, 6, 5, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 6, 5]) == [5, 6, 5, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 3, 5, 2, 6, 4]) == [7, 2, 6, 3, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 3, 5, 2, 6, 4]) == [7, 2, 6, 3, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 1, 5, 2, 4]) == [6, 3, 5, 3, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 1, 5, 2, 4]) == [6, 3, 5, 3, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 2, 8, 6, 4, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 5, 10, 9, 2, 8, 7, 2, 6, 5, 2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 2, 8, 6, 4, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 5, 10, 9, 2, 8, 7, 2, 6, 5, 2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 7, 3, 6, 2, 5, 4]) == [8, 6, 7, 5, 6, 4, 5, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 7, 3, 6, 2, 5, 4]) == [8, 6, 7, 5, 6, 4, 5, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 4, 5]) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 4, 5]) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 4, 6, 2, 5, 1, 3]) == [7, 5, 6, 4, 5, 2, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 4, 6, 2, 5, 1, 3]) == [7, 5, 6, 4, 5, 2, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 5, 3, 6, 4, 2]) == [7, 3, 6, 2, 5, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 5, 3, 6, 4, 2]) == [7, 3, 6, 2, 5, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 2, 5, 4, 1]) == [6, 3, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 2, 5, 4, 1]) == [6, 3, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 3, 1, 4]) == [5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 3, 1, 4]) == [5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2]) == [10, 4, 9, 8, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2]) == [10, 4, 9, 8, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 6, 4, 3, 5, 1, 7]) == [2, 6, 2, 5, 2, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 6, 4, 3, 5, 1, 7]) == [2, 6, 2, 5, 2, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 4, 6, 5]) == [5, 6, 5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 4, 6, 5]) == [5, 6, 5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 2, 3, 4, 5, 6, 7]) == [8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 2, 3, 4, 5, 6, 7]) == [8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 3, 1, 4, 6, 7, 8, 9, 10]) == [5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 3, 1, 4, 6, 7, 8, 9, 10]) == [5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 5, 4]) == [4, 5, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 5, 4]) == [4, 5, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 5, 2, 4, 6, 1, 3]) == [7, 3, 6, 5, 3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 5, 2, 4, 6, 1, 3]) == [7, 3, 6, 5, 3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 1, 3, 5]) == [2, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 1, 3, 5]) == [2, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 2, 4]) == [5, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 2, 4]) == [5, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 7, 8, 6, 7, 5, 6, 4, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 7, 8, 6, 7, 5, 6, 4, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 6, 1, 2, 4]) == [3, 6, 4, 5, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 6, 1, 2, 4]) == [3, 6, 4, 5, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 5, 2, 3, 6]) == [3, 5, 3, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 5, 2, 3, 6]) == [3, 5, 3, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 1, 8, 5, 2, 7, 4]) == [4, 8, 2, 7, 2, 6, 3, 5, 3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 1, 8, 5, 2, 7, 4]) == [4, 8, 2, 7, 2, 6, 3, 5, 3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 2, 4, 6]) == [3, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 2, 4, 6]) == [3, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 7, 4, 3, 5, 1, 6, 8, 9, 10]) == [2, 7, 6, 4, 5, 3, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 7, 4, 3, 5, 1, 6, 8, 9, 10]) == [2, 7, 6, 4, 5, 3, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 3, 7, 5, 2, 6, 4]) == [8, 5, 7, 4, 6, 5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 3, 7, 5, 2, 6, 4]) == [8, 5, 7, 4, 6, 5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 2, 9, 3, 8, 4, 7, 5, 10, 6, 1]) == [11, 3, 10, 2, 9, 6, 8, 6, 7, 4, 6, 5, 3, 4, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 2, 9, 3, 8, 4, 7, 5, 10, 6, 1]) == [11, 3, 10, 2, 9, 6, 8, 6, 7, 4, 6, 5, 3, 4, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 5, 4, 2, 1]) == [6, 4, 5, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 5, 4, 2, 1]) == [6, 4, 5, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 3, 4, 5, 6, 7, 8, 9, 2]) == [10, 2, 9, 7, 8, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 3, 4, 5, 6, 7, 8, 9, 2]) == [10, 2, 9, 7, 8, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2]) == [9, 4, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2]) == [9, 4, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5]) == [2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5]) == [2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 9, 5, 1, 8, 3, 7, 4, 6]) == [2, 9, 5, 8, 6, 7, 5, 6, 4, 5, 2, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 9, 5, 1, 8, 3, 7, 4, 6]) == [2, 9, 5, 8, 6, 7, 5, 6, 4, 5, 2, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 9, 7, 3, 10, 2, 4, 8, 6]) == [6, 10, 7, 9, 4, 8, 6, 7, 6, 4, 5, 3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 9, 7, 3, 10, 2, 4, 8, 6]) == [6, 10, 7, 9, 4, 8, 6, 7, 6, 4, 5, 3, 4, 2]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [2, 1, 3, 4, 5]) == [2]
    assert candidate(arr = [4, 3, 2, 1]) == [4]
    assert candidate(arr = [5, 4, 3, 2, 1]) == [5]
    assert candidate(arr = [3, 1, 2]) == [3, 2]
    assert candidate(arr = [1, 5, 3, 4, 2]) == [2, 5, 2, 4, 2, 3, 2]
    assert candidate(arr = [2, 3, 4, 1, 5]) == [3, 4]
    assert candidate(arr = [1, 2, 3]) == []
    assert candidate(arr = [1, 5, 4, 3, 2]) == [2, 5, 3, 4]
    assert candidate(arr = [1]) == []
    assert candidate(arr = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
    assert candidate(arr = [2, 1]) == [2]
    assert candidate(arr = [3, 2, 4, 1]) == [3, 4, 2, 3, 2]
    assert candidate(arr = [1, 3, 2]) == [2, 3, 2]
    assert candidate(arr = [6, 3, 5, 1, 2, 4]) == [6, 4, 5, 2, 4]
    assert candidate(arr = [2, 5, 1, 3, 4]) == [2, 5, 4, 2]
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [11, 10, 5, 9, 8, 7, 2, 6, 2, 4, 3, 2]
    assert candidate(arr = [3, 1, 4, 2, 6, 5]) == [5, 6, 5, 2, 4, 3, 2]
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]
    assert candidate(arr = [7, 1, 2, 6, 4, 5, 3]) == [7, 4, 6, 4, 5, 4, 3]
    assert candidate(arr = [1, 10, 3, 5, 7, 9, 2, 4, 8, 6]) == [2, 10, 5, 9, 6, 8, 6, 7, 6, 5, 2, 4, 3, 2]
    assert candidate(arr = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]
    assert candidate(arr = [2, 4, 1, 3]) == [2, 4, 3, 2]
    assert candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == [6]
    assert candidate(arr = [7, 1, 8, 2, 9, 3, 10, 4, 5, 6]) == [7, 10, 8, 9, 7, 8, 6, 7, 4, 6, 2, 5, 3]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]
    assert candidate(arr = [8, 5, 10, 9, 3, 7, 6, 4, 2, 1]) == [3, 10, 7, 9, 2, 8, 2, 7, 5, 6, 2, 5, 4, 3, 2]
    assert candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 8, 9, 7, 8, 6, 7, 5, 6, 4]
    assert candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]) == [9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(arr = [6, 5, 3, 1, 2, 4]) == [6, 4, 3, 2]
    assert candidate(arr = [2, 1, 4, 3, 6, 5]) == [5, 6, 5, 2, 4, 2]
    assert candidate(arr = [3, 1, 4, 2]) == [3, 4, 2, 3]
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]
    assert candidate(arr = [8, 6, 4, 2, 1, 3, 5, 7]) == [8, 7, 6, 5, 4, 3, 2]
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]
    assert candidate(arr = [8, 6, 7, 5, 3, 1, 4, 9, 2, 10]) == [8, 9, 2, 8, 5, 7, 2, 6, 5, 2, 4, 3, 2]
    assert candidate(arr = [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]) == [6, 10, 4, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(arr = [7, 10, 4, 8, 5, 9, 1, 6, 2, 3]) == [2, 10, 5, 9, 3, 8, 6, 7, 3, 6, 5, 2, 4, 3]
    assert candidate(arr = [5, 1, 4, 2, 3]) == [5, 3, 4, 2, 3, 2]
    assert candidate(arr = [5, 3, 1, 4, 2]) == [5, 2, 4, 3, 2]
    assert candidate(arr = [10, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == [10, 2, 9, 6, 7, 6, 2, 5, 2]
    assert candidate(arr = [8, 5, 9, 1, 7, 3, 4, 2, 6]) == [3, 9, 7, 8, 6, 7, 3, 6, 2, 4]
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20]
    assert candidate(arr = [5, 4, 2, 3, 1]) == [5, 2, 3, 2]
    assert candidate(arr = [7, 1, 6, 2, 5, 3, 4]) == [7, 5, 6, 4, 5, 3, 4, 3]
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]
    assert candidate(arr = [4, 6, 3, 5, 2, 1]) == [2, 6, 3, 5, 4, 2]
    assert candidate(arr = [6, 4, 2, 1, 3, 5]) == [6, 5, 4, 3, 2]
    assert candidate(arr = [2, 7, 4, 1, 8, 3, 6, 5]) == [5, 8, 5, 7, 4, 6, 2, 3]
    assert candidate(arr = [3, 6, 1, 7, 5, 4, 2]) == [4, 7, 5, 6, 4, 5, 3, 2]
    assert candidate(arr = [6, 1, 5, 2, 4, 3]) == [6, 4, 5, 3, 4, 2]
    assert candidate(arr = [1, 4, 3, 2, 5, 6, 7, 8, 9, 10]) == [2, 4, 2, 3]
    assert candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == [3, 8, 3, 7, 3, 6, 4, 3]
    assert candidate(arr = [1, 3, 2, 5, 4]) == [4, 5, 4, 2, 3]
    assert candidate(arr = [6, 5, 4, 3, 2, 1, 7, 8, 9]) == [6]
    assert candidate(arr = [1, 3, 2, 4, 6, 5]) == [5, 6, 5, 4, 2, 3, 2]
    assert candidate(arr = [7, 1, 3, 5, 2, 6, 4]) == [7, 2, 6, 3, 5, 4, 3, 2]
    assert candidate(arr = [6, 3, 1, 5, 2, 4]) == [6, 3, 5, 3, 4, 2, 3]
    assert candidate(arr = [10, 2, 8, 6, 4, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 5, 10, 9, 2, 8, 7, 2, 6, 5, 2, 4, 3, 2]
    assert candidate(arr = [8, 1, 7, 3, 6, 2, 5, 4]) == [8, 6, 7, 5, 6, 4, 5, 2, 3]
    assert candidate(arr = [3, 1, 2, 4, 5]) == [3, 2]
    assert candidate(arr = [7, 4, 6, 2, 5, 1, 3]) == [7, 5, 6, 4, 5, 2, 4, 2, 3, 2]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]
    assert candidate(arr = [7, 1, 5, 3, 6, 4, 2]) == [7, 3, 6, 2, 5, 4, 2, 3, 2]
    assert candidate(arr = [6, 3, 2, 5, 4, 1]) == [6, 3, 5, 3]
    assert candidate(arr = [5, 2, 3, 1, 4]) == [5, 4, 2, 3]
    assert candidate(arr = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2]) == [10, 4, 9, 8, 6, 5, 4, 3, 2]
    assert candidate(arr = [2, 6, 4, 3, 5, 1, 7]) == [2, 6, 2, 5, 2, 4, 2, 3, 2]
    assert candidate(arr = [2, 3, 1, 4, 6, 5]) == [5, 6, 5, 4, 2, 3]
    assert candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]
    assert candidate(arr = [8, 1, 2, 3, 4, 5, 6, 7]) == [8, 7]
    assert candidate(arr = [5, 2, 3, 1, 4, 6, 7, 8, 9, 10]) == [5, 4, 2, 3]
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [8, 9, 8, 2, 7, 4, 5, 4, 2, 3]
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15]
    assert candidate(arr = [2, 3, 1, 5, 4]) == [4, 5, 4, 2, 3, 2]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [9]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [9]
    assert candidate(arr = [3, 5, 4, 1, 2]) == [2, 5, 3, 4, 3]
    assert candidate(arr = [7, 5, 2, 4, 6, 1, 3]) == [7, 3, 6, 5, 3, 4, 2]
    assert candidate(arr = [2, 4, 1, 3, 5]) == [2, 4, 3, 2]
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8]) == [7]
    assert candidate(arr = [5, 1, 3, 2, 4]) == [5, 4, 2, 3, 2]
    assert candidate(arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [12]
    assert candidate(arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 7, 8, 6, 7, 5, 6, 4, 5, 4]
    assert candidate(arr = [5, 3, 6, 1, 2, 4]) == [3, 6, 4, 5, 2, 4]
    assert candidate(arr = [4, 1, 5, 2, 3, 6]) == [3, 5, 3, 4, 2, 3, 2]
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9]
    assert candidate(arr = [3, 6, 1, 8, 5, 2, 7, 4]) == [4, 8, 2, 7, 2, 6, 3, 5, 3, 4, 2]
    assert candidate(arr = [1, 3, 5, 2, 4, 6]) == [3, 5, 4, 3, 2]
    assert candidate(arr = [2, 7, 4, 3, 5, 1, 6, 8, 9, 10]) == [2, 7, 6, 4, 5, 3, 4, 3, 2]
    assert candidate(arr = [8, 1, 3, 7, 5, 2, 6, 4]) == [8, 5, 7, 4, 6, 5, 4, 2]
    assert candidate(arr = [11, 2, 9, 3, 8, 4, 7, 5, 10, 6, 1]) == [11, 3, 10, 2, 9, 6, 8, 6, 7, 4, 6, 5, 3, 4, 2, 3, 2]
    assert candidate(arr = [6, 3, 5, 4, 2, 1]) == [6, 4, 5, 3, 2]
    assert candidate(arr = [10, 1, 3, 4, 5, 6, 7, 8, 9, 2]) == [10, 2, 9, 7, 8, 2]
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == [7]
    assert candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2]) == [9, 4, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(arr = [1, 3, 2, 4, 5]) == [2, 3, 2]
    assert candidate(arr = [2, 9, 5, 1, 8, 3, 7, 4, 6]) == [2, 9, 5, 8, 6, 7, 5, 6, 4, 5, 2, 4, 2, 3]
    assert candidate(arr = [5, 1, 9, 7, 3, 10, 2, 4, 8, 6]) == [6, 10, 7, 9, 4, 8, 6, 7, 6, 4, 5, 3, 4, 2]


