def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 3, 3, 4, 4, 4, 4],target = 2) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 3, 3, 4, 4, 4, 4],target = 2) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 5) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 5) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 7, 8, 8, 10],target = 8) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 7, 8, 8, 10],target = 8) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -3, 0, 3, 5, 9, 10],target = 3) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -3, 0, 3, 5, 9, 10],target = 3) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4, 5],target = 2) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4, 5],target = 2) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6],target = 4) == [4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6],target = 4) == [4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 7) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 7) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 7, 8, 8, 10],target = 6) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 7, 8, 8, 10],target = 6) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 5) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 5) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 2) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 2) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 10) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 10) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],target = 2) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],target = 2) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == [19, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == [19, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 4) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 4) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 6) == [5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 6) == [5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = 15) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = 15) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 5) == [9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 5) == [9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5],target = 2) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5],target = 2) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 5) == [6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 5) == [6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 7) == [11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 7) == [11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 10],target = 5) == [6, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 10],target = 5) == [6, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 4) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 4) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 4) == [15, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 4) == [15, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],target = 3) == [4, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],target = 3) == [4, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 3) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 3) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -100) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -100) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9],target = 4) == [4, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9],target = 4) == [4, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 16) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 16) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7],target = 5) == [7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7],target = 5) == [7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 2) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 2) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10],target = 3) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10],target = 3) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 2) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 2) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 10) == [22, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 10) == [22, 22]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -6) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -6) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 3, 5, 7, 9],target = 3) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 3, 5, 7, 9],target = 3) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10],target = 5) == [7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10],target = 5) == [7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 22) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 22) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7],target = 4) == [4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7],target = 4) == [4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 2) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 2) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10],target = 7) == [18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10],target = 7) == [18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -5) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -5) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -90) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -90) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 1) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 1) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 20) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 20) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 13) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 13) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 2) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 2) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -1, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = -5) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -1, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = -5) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8],target = 5) == [8, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8],target = 5) == [8, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 5) == [7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 5) == [7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10],target = 10) == [12, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10],target = 10) == [12, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 10) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 10) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 8) == [13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 8) == [13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 31]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 0) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 0) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -10) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -10) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 7) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 7) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = -3) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = -3) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 29) == [14, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 29) == [14, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 5) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 5) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 0) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 0) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 21) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 21) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 2) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 2) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [1, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [1, 21]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],target = 3) == [6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],target = 3) == [6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 25) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 25) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 5) == [7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 5) == [7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 25) == [12, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 25) == [12, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 7) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 7) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 9) == [8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 9) == [8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 8) == [13, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 8) == [13, 16]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 5) == [8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 5) == [8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 0, 0, 1, 2, 3, 3, 3, 3, 4, 5, 6],target = -5) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 0, 0, 1, 2, 3, 3, 3, 3, 4, 5, 6],target = -5) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 5) == [12, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 5) == [12, 16]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 1) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 1) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 3) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 3) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 9) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 9) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 29]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 0) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 0) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 25) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 25) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 10) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 10) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 11) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 11) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 11) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 11) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 3) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 3) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -10) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -10) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [3, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [3, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 7) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 7) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 10]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]
    assert candidate(nums = [2, 2, 2, 2, 3, 3, 4, 4, 4, 4],target = 2) == [0, 3]
    assert candidate(nums = [1, 2, 3, 4, 5],target = 5) == [4, 4]
    assert candidate(nums = [5, 7, 7, 8, 8, 10],target = 8) == [3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 1) == [0, 0]
    assert candidate(nums = [-10, -5, -3, 0, 3, 5, 9, 10],target = 3) == [4, 4]
    assert candidate(nums = [1, 3, 5, 7, 9],target = 0) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 5],target = 2) == [1, 3]
    assert candidate(nums = [1],target = 1) == [0, 0]
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6],target = 4) == [4, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 7) == [6, 6]
    assert candidate(nums = [5, 7, 7, 8, 8, 10],target = 6) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1) == [0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],target = 5) == [4, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]
    assert candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 4]
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]
    assert candidate(nums = [1, 3, 5, 7, 9],target = 2) == [-1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 9]
    assert candidate(nums = [],target = 0) == [-1, -1]
    assert candidate(nums = [1],target = 0) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5],target = 1) == [0, 0]
    assert candidate(nums = [1, 3, 5, 7, 9],target = 10) == [-1, -1]
    assert candidate(nums = [1],target = 2) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == [19, 19]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 4) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 6) == [5, 5]
    assert candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = 15) == [-1, -1]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 5) == [9, 11]
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5],target = 2) == [1, 3]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 5) == [6, 8]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 7) == [11, 12]
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 10],target = 5) == [6, 9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 0) == [-1, -1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 4) == [-1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 4) == [15, 19]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == [0, 9]
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],target = 3) == [4, 7]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 7]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 3) == [3, 4]
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -100) == [0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9],target = 4) == [4, 9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 0) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 16) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7],target = 5) == [7, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 2) == [2, 4]
    assert candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10],target = 3) == [2, 5]
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5],target = 2) == [1, 4]
    assert candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 2) == [1, 1]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [5, 6]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 10) == [22, 22]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -6) == [-1, -1]
    assert candidate(nums = [1, 3, 3, 3, 3, 5, 7, 9],target = 3) == [1, 4]
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10],target = 5) == [7, 9]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 22) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7],target = 4) == [4, 6]
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -1) == [-1, -1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7, 7]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 2) == [1, 1]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10],target = 7) == [18, 19]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -5) == [1, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -90) == [10, 10]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 1) == [0, 1]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 0) == [-1, -1]
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 20) == [6, 6]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 1) == [0, 0]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 13) == [6, 6]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 2) == [1, 2]
    assert candidate(nums = [-10, -5, -5, -1, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = -5) == [1, 2]
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8],target = 5) == [8, 11]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 5) == [7, 8]
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10],target = 10) == [12, 15]
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 20]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 10) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 8) == [13, 14]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9, 9]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 1) == [0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9, 9]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 19]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 31]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == [-1, -1]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 0) == [4, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14, 14]
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [1, 12]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [17, 18]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [9, 10]
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -10) == [0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 7) == [6, 6]
    assert candidate(nums = [-10, -8, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13],target = -3) == [3, 3]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 29) == [14, 14]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 5) == [4, 4]
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 0) == [2, 2]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 21) == [10, 10]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 2) == [1, 2]
    assert candidate(nums = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [1, 21]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],target = 3) == [6, 8]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 14]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [-1, -1]
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = 25) == [-1, -1]
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 5) == [7, 10]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 25) == [12, 12]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 7) == [6, 6]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 9) == [8, 8]
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9],target = 8) == [13, 16]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 14]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10],target = 5) == [8, 12]
    assert candidate(nums = [-10, -5, -5, -5, 0, 0, 0, 1, 2, 3, 3, 3, 3, 4, 5, 6],target = -5) == [1, 3]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 0) == [-1, -1]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 2) == [0, 9]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10],target = 5) == [12, 16]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 1) == [0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 6],target = 3) == [2, 5]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 6) == [10, 11]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = 9) == [9, 9]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 29]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 0) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 25) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 10) == [9, 9]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 11) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 11) == [10, 10]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 3) == [-1, -1]
    assert candidate(nums = [-10, -5, -5, -5, 0, 3, 5, 5, 5, 9],target = -10) == [0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == [0, 4]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5],target = 3) == [3, 8]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6],target = 7) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4, 4]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == [0, 10]


