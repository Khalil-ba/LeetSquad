def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1]) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1]) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0]) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0]) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [11, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [11, 16]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [4, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [4, 13]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [6, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [6, 11]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]) == [2, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]) == [2, 13]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]) == [2, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]) == [2, 12]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [5, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [5, 11]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [3, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [3, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [7, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [7, 14]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [3, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [3, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 19]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [2, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [2, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [3, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [3, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [5, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [5, 14]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]) == [6, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]) == [6, 12]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [6, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [6, 15]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 12]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]) == [3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]) == [3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == [7, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == [7, 14]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]) == [7, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]) == [7, 16]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == [4, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == [4, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [5, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [5, 12]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 0, 1, 0, 1]) == [0, 3]
    assert candidate(arr = [0, 0, 0]) == [0, 2]
    assert candidate(arr = [1, 1, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0]) == [2, 6]
    assert candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [2, 8]
    assert candidate(arr = [0, 0, 0, 0, 0, 0]) == [0, 5]
    assert candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 0, 1]) == [0, 2]
    assert candidate(arr = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [11, 16]
    assert candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [4, 13]
    assert candidate(arr = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [6, 11]
    assert candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]) == [2, 13]
    assert candidate(arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]) == [2, 12]
    assert candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [4, 8]
    assert candidate(arr = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [5, 11]
    assert candidate(arr = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [3, 8]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [7, 14]
    assert candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [3, 10]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 19]
    assert candidate(arr = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == [2, 9]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [3, 8]
    assert candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [5, 14]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [2, 7]
    assert candidate(arr = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]) == [6, 12]
    assert candidate(arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == [0, 13]
    assert candidate(arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [6, 15]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 12]
    assert candidate(arr = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]) == [3, 9]
    assert candidate(arr = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == [7, 14]
    assert candidate(arr = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]) == [7, 16]
    assert candidate(arr = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]) == [-1, -1]
    assert candidate(arr = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == [4, 10]
    assert candidate(arr = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == [-1, -1]
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == [-1, -1]
    assert candidate(arr = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == [-1, -1]
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [5, 12]


