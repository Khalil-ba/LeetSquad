def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1]) == [1, 1, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1]) == [1, 1, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],freq = [-1, -1, -1, -1, -1]) == [-1, -2, -3, -4, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],freq = [-1, -1, -1, -1, -1]) == [-1, -2, -3, -4, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 1],freq = [3, 2, -3, 1]) == [3, 3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 1],freq = [3, 2, -3, 1]) == [3, 3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],freq = [5, -2, 3, -6, 2]) == [5, 3, 6, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],freq = [5, -2, 3, -6, 2]) == [5, 3, 6, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 3],freq = [2, -2, 1]) == [2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 3],freq = [2, -2, 1]) == [2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],freq = [5, -1, -1, -1, -3]) == [5, 4, 3, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],freq = [5, -1, -1, -1, -3]) == [5, 4, 3, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 2, 1, -1, -2, 3]) == [1, 2, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 2, 1, -1, -2, 3]) == [1, 2, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 3],freq = [1, 1, -2, 1, 1, 1]) == [1, 2, 0, 1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 3],freq = [1, 1, -2, 1, 1, 1]) == [1, 2, 0, 1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3],freq = [2, -1, 2, -1, 2, -1]) == [2, 1, 2, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3],freq = [2, -1, 2, -1, 2, -1]) == [2, 1, 2, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 30],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 30],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000],freq = [100000, -50000, -50000, 1]) == [100000, 50000, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000],freq = [100000, -50000, -50000, 1]) == [100000, 50000, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],freq = [1, 1, -1, 1, -1, -1, 1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],freq = [1, 1, -1, 1, -1, -1, 1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [10, -5, 20, -10, 30, -15, 40, -20, 50, -25]) == [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [10, -5, 20, -10, 30, -15, 40, -20, 50, -25]) == [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [1, 1, -2, 1, 1, -2, 1, 1, -2, 1, 1, -2]) == [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [1, 1, -2, 1, 1, -2, 1, 1, -2, 1, 1, -2]) == [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],freq = [1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],freq = [1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [1, -1, 1, 1, -1, 1, 1, 1, -3]) == [1, 0, 1, 2, 1, 1, 2, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [1, -1, 1, 1, -1, 1, 1, 1, -3]) == [1, 0, 1, 2, 1, 1, 2, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 60, 90, 150, 150, 150, 240, 340]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 60, 90, 150, 150, 150, 240, 340]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == [10, 20, 30, 40, 50, 50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == [10, 20, 30, 40, 50, 50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 10, 10, 10, 10, -5, -5, -5, -5, -5]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 10, 10, 10, 10, -5, -5, -5, -5, -5]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == [-1, 2, 2, 4, 4, 6, 6, 8, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == [-1, 2, 2, 4, 4, 6, 6, 8, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == [-10, 20, 20, 40, 40, 60, 60, 80, 80, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == [-10, 20, 20, 40, 40, 60, 60, 80, 80, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, -100000, 100000, -100000, 100000]) == [100000, 100000, 100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, -100000, 100000, -100000, 100000]) == [100000, 100000, 100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7],freq = [1, -1, 2, -2, 3, -3, 4]) == [1, 0, 2, 0, 3, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7],freq = [1, -1, 2, -2, 3, -3, 4]) == [1, 0, 2, 0, 3, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],freq = [100, -50, 200, -100, 300, -150]) == [100, 100, 200, 200, 300, 300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],freq = [100, -50, 200, -100, 300, -150]) == [100, 100, 200, 200, 300, 300]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == [2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == [2, 0, 3, 0, 4, 0, 5, 0, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],freq = [1, 1, -1, 1, 1, -2, 1, 1, 1, -3]) == [1, 1, 1, 1, 2, 1, 1, 2, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],freq = [1, 1, -1, 1, 1, -2, 1, 1, 1, -3]) == [1, 1, 1, 1, 2, 1, 1, 2, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],freq = [10, 20, 30, -5, -10, -15, 5, 10, 15, -25]) == [10, 20, 30, 30, 30, 15, 15, 20, 30, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],freq = [10, 20, 30, -5, -10, -15, 5, 10, 15, -25]) == [10, 20, 30, 30, 30, 15, 15, 20, 30, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],freq = [10, -5, 7, -3, 2, 8, -2, 4, -1, 6, -4, 3, -2, 1]) == [10, 5, 7, 5, 6, 8, 6, 10, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],freq = [10, -5, 7, -3, 2, 8, -2, 4, -1, 6, -4, 3, -2, 1]) == [10, 5, 7, 5, 6, 8, 6, 10, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],freq = [100, -50, 50, -25, 25, -12, -6, -3, -1, 1]) == [100, 100, 150, 150, 175, 175, 169, 169, 168, 168]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],freq = [100, -50, 50, -25, 25, -12, -6, -3, -1, 1]) == [100, 100, 150, 150, 175, 175, 169, 169, 168, 168]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000],freq = [100000, -50000, 50000, -25000, 25000]) == [100000, 50000, 100000, 75000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000],freq = [100000, -50000, 50000, -25000, 25000]) == [100000, 50000, 100000, 75000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -2, 5, -3, 7, -1, 4, -6, 2, -8]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -2, 5, -3, 7, -1, 4, -6, 2, -8]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1000, 1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000, -1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1000, 1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000, -1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],freq = [1000, 2000, 3000, 4000, 5000]) == [1000, 2000, 3000, 4000, 5000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],freq = [1000, 2000, 3000, 4000, 5000]) == [1000, 2000, 3000, 4000, 5000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 50000, -25000, 25000, -12500, 12500, -6250, 6250, -3125]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 50000, -25000, 25000, -12500, 12500, -6250, 6250, -3125]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -50, 200, -100, 300, -150, 400, -200, 500, -250]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -50, 200, -100, 300, -150, 400, -200, 500, -250]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],freq = [10, -5, 20, -10, 15, -20, 25, -15, 30, -30]) == [10, 10, 20, 20, 20, 10, 25, 25, 30, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],freq = [10, -5, 20, -10, 15, -20, 25, -15, 30, -30]) == [10, 10, 20, 20, 20, 10, 25, 25, 30, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],freq = [1000, -500, 1500, -2000, 2500]) == [1000, 1000, 1500, 1500, 2500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],freq = [1000, -500, 1500, -2000, 2500]) == [1000, 1000, 1500, 1500, 2500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [50000, -50000, 30000, -30000, 20000]) == [50000, 50000, 50000, 50000, 50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [50000, -50000, 30000, -30000, 20000]) == [50000, 50000, 50000, 50000, 50000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],freq = [2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],freq = [2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [50000, -25000, 12500, -6250, 3125, -1562, 781, -390, 195, -97]) == [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [50000, -25000, 12500, -6250, 3125, -1562, 781, -390, 195, -97]) == [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [2, 2, 2, -1, -1, -1, 1, 1, 1]) == [2, 4, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [2, 2, 2, -1, -1, -1, 1, 1, 1]) == [2, 4, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],freq = [100, -100, 50, 200, -200, 100, 300, -300, 150]) == [100, 0, 50, 200, 50, 100, 300, 100, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],freq = [100, -100, 50, 200, -200, 100, 300, -300, 150]) == [100, 0, 50, 200, 50, 100, 300, 100, 150]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],freq = [10, -10, 20, -20, 30]) == [10, 10, 20, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],freq = [10, -10, 20, -20, 30]) == [10, 10, 20, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [100, -10, -10, -10, -10, -10, -10, -10, -10, -100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, -80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [100, -10, -10, -10, -10, -10, -10, -10, -10, -100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, -80]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3],freq = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3, 3, 4, 6, 6, 6, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3],freq = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3, 3, 4, 6, 6, 6, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],freq = [50, 100, -50, -100, 50]) == [50, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],freq = [50, 100, -50, -100, 50]) == [50, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [10, 20, -30, 15, 25, -40, 20, 30, -50, 10, 20, -30]) == [10, 30, 0, 15, 40, 0, 20, 50, 0, 10, 30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [10, 20, -30, 15, 25, -40, 20, 30, -50, 10, 20, -30]) == [10, 30, 0, 15, 40, 0, 20, 50, 0, 10, 30, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [10, 20, 30, -10, -20, -30, 40, 50, -40, -50]) == [10, 30, 60, 50, 30, 0, 40, 90, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [10, 20, 30, -10, -20, -30, 40, 50, -40, -50]) == [10, 30, 60, 50, 30, 0, 40, 90, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1],freq = [1, -1, 1, -1, 1, -1, 1]) == [1, 1, 2, 2, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1],freq = [1, -1, 1, -1, 1, -1, 1]) == [1, 1, 2, 2, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 30, 70, 70, 110, 110, 150, 150, 190]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 30, 70, 70, 110, 110, 150, 150, 190]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == [-10, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == [-10, 9, 9, 9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, 99999, 99998, 99997, 99996]) == [100000, 100000, 100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, 99999, 99998, 99997, 99996]) == [100000, 100000, 100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1]) == [1, 1, 2, 2, 2, 2]
    assert candidate(nums = [1, 1, 1, 1, 1],freq = [-1, -1, -1, -1, -1]) == [-1, -2, -3, -4, -5]
    assert candidate(nums = [2, 3, 2, 1],freq = [3, 2, -3, 1]) == [3, 3, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [10, 10, 10, 10, 10],freq = [5, -2, 3, -6, 2]) == [5, 3, 6, 0, 2]
    assert candidate(nums = [5, 5, 3],freq = [2, -2, 1]) == [2, 0, 1]
    assert candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 10, 10, 10, 10],freq = [5, -1, -1, -1, -3]) == [5, 4, 3, 2, -1]
    assert candidate(nums = [1, 2, 2, 3, 3, 3],freq = [1, 2, 1, -1, -2, 3]) == [1, 2, 3, 3, 3, 3]
    assert candidate(nums = [1, 1, 1, 2, 2, 3],freq = [1, 1, -2, 1, 1, 1]) == [1, 2, 0, 1, 2, 2]
    assert candidate(nums = [1, 1, 2, 2, 3, 3],freq = [2, -1, 2, -1, 2, -1]) == [2, 1, 2, 1, 2, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
    assert candidate(nums = [10, 20, 10, 30, 20, 30],freq = [1, 1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1, 2]
    assert candidate(nums = [100000, 100000, 100000, 100000],freq = [100000, -50000, -50000, 1]) == [100000, 50000, 0, 1]
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],freq = [1, 1, -1, 1, -1, -1, 1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [10, -5, 20, -10, 30, -15, 40, -20, 50, -25]) == [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [1, 1, -2, 1, 1, -2, 1, 1, -2, 1, 1, -2]) == [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    assert candidate(nums = [1, 3, 5, 7, 9],freq = [1, -1, 1, -1, 1]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [1, -1, 1, 1, -1, 1, 1, 1, -3]) == [1, 0, 1, 2, 1, 1, 2, 3, 1]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 60, 90, 150, 150, 150, 240, 340]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == [10, 20, 30, 40, 50, 50, 50, 50, 50, 50]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 10, 10, 10, 10, -5, -5, -5, -5, -5]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == [-1, 2, 2, 4, 4, 6, 6, 8, 8, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == [-10, 20, 20, 40, 40, 60, 60, 80, 80, 100]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, -100000, 100000, -100000, 100000]) == [100000, 100000, 100000, 100000, 100000]
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7],freq = [1, -1, 2, -2, 3, -3, 4]) == [1, 0, 2, 0, 3, 0, 4]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 10, 15, 20, 25, 30],freq = [100, -50, 200, -100, 300, -150]) == [100, 100, 200, 200, 300, 300]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == [2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],freq = [1, 1, -1, 1, 1, -2, 1, 1, 1, -3]) == [1, 1, 1, 1, 2, 1, 1, 2, 3, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],freq = [10, 20, 30, -5, -10, -15, 5, 10, 15, -25]) == [10, 20, 30, 30, 30, 15, 15, 20, 30, 30]
    assert candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],freq = [10, -5, 7, -3, 2, 8, -2, 4, -1, 6, -4, 3, -2, 1]) == [10, 5, 7, 5, 6, 8, 6, 10, 9, 9, 9, 9, 9, 9]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],freq = [100, -50, 50, -25, 25, -12, -6, -3, -1, 1]) == [100, 100, 150, 150, 175, 175, 169, 169, 168, 168]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],freq = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000, 100000, -50000]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],freq = [100000, -50000, 50000, -25000, 25000]) == [100000, 50000, 100000, 75000, 100000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -2, 5, -3, 7, -1, 4, -6, 2, -8]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1000, 1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000, -1000]) == [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    assert candidate(nums = [10, 20, 30, 40, 50],freq = [1000, 2000, 3000, 4000, 5000]) == [1000, 2000, 3000, 4000, 5000]
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100000, -50000, 50000, -25000, 25000, -12500, 12500, -6250, 6250, -3125]) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -50, 200, -100, 300, -150, 400, -200, 500, -250]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],freq = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]
    assert candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],freq = [10, -5, 20, -10, 15, -20, 25, -15, 30, -30]) == [10, 10, 20, 20, 20, 10, 25, 25, 30, 30]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    assert candidate(nums = [100, 200, 300, 400, 500],freq = [1000, -500, 1500, -2000, 2500]) == [1000, 1000, 1500, 1500, 2500]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [50000, -50000, 30000, -30000, 20000]) == [50000, 50000, 50000, 50000, 50000]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [5, 10, 15, 20, 25],freq = [2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5],freq = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],freq = [50000, -25000, 12500, -6250, 3125, -1562, 781, -390, 195, -97]) == [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [2, 2, 2, -1, -1, -1, 1, 1, 1]) == [2, 4, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],freq = [100, -100, 50, 200, -200, 100, 300, -300, 150]) == [100, 0, 50, 200, 50, 100, 300, 100, 150]
    assert candidate(nums = [10, 20, 30, 40, 50],freq = [10, -10, 20, -20, 30]) == [10, 10, 20, 20, 30]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],freq = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500]) == [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [100, -10, -10, -10, -10, -10, -10, -10, -10, -100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, -80]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3],freq = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3, 3, 4, 6, 6, 6, 9]
    assert candidate(nums = [100, 200, 300, 400, 500],freq = [50, 100, -50, -100, 50]) == [50, 100, 100, 100, 100]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],freq = [10, 20, -30, 15, 25, -40, 20, 30, -50, 10, 20, -30]) == [10, 30, 0, 15, 40, 0, 20, 50, 0, 10, 30, 0]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [100, 200, 300, 400, 500],freq = [-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],freq = [10, 20, 30, -10, -20, -30, 40, 50, -40, -50]) == [10, 30, 60, 50, 30, 0, 40, 90, 50, 0]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1],freq = [1, -1, 1, -1, 1, -1, 1]) == [1, 1, 2, 2, 3, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],freq = [1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],freq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 30, 70, 70, 110, 110, 150, 150, 190]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == [-10, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, 1, 1, 1, 1, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],freq = [100000, 99999, 99998, 99997, 99996]) == [100000, 100000, 100000, 100000, 100000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],freq = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


