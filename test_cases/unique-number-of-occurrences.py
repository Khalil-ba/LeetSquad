def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -1, -2, -2, -3, -3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -1, -2, -2, -3, -3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -1000, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -1000, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 1, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 1, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, -1, 1, -1, 1, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, -1, 1, -1, 1, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -1000, 1000, -1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -1000, 1000, -1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, -1000, -1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, -1000, -1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -2, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -2, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000, 999, 999, 998, 997, 996, 995, 994]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000, 999, 999, 998, 997, 996, 995, 994]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -50, -50, -50, -50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -50, -50, -50, -50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -20, -30, -40, -50, -50, -40, -30, -20, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -20, -30, -40, -50, -50, -40, -30, -20, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -1000, 500, -500, 0, 0, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -1000, 500, -500, 0, 0, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -5, -5, -5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -5, -5, -5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 10, 30, 40, 40, 50, 50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 10, 30, 40, 40, 50, 50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, 0, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, 0, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 20, 10, 30, 40, 40, 40, 50, 50, 50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 20, 10, 30, 40, 40, 40, 50, 50, 50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
    assert candidate(arr = [1, 2]) == False
    assert candidate(arr = [5]) == True
    assert candidate(arr = [5, 5, 5, 5, 5]) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3]) == False
    assert candidate(arr = [-1, -1, -2, -2, -3, -3]) == False
    assert candidate(arr = [5, 5, 5, 5]) == True
    assert candidate(arr = [1]) == True
    assert candidate(arr = [1000, -1000, 0]) == False
    assert candidate(arr = [1, 2, 2, 1, 1, 3]) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == True
    assert candidate(arr = [1, 2, 3, 4, 5]) == False
    assert candidate(arr = [0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]) == True
    assert candidate(arr = [1, -1, 1, -1, 1, -1]) == False
    assert candidate(arr = [1000, -1000, 1000, -1000]) == False
    assert candidate(arr = [1, 2, 3, 2, 1]) == False
    assert candidate(arr = [1000, 1000, -1000, -1000]) == False
    assert candidate(arr = [-1, -2, -3, -2, -1]) == False
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3]) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == False
    assert candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9]) == True
    assert candidate(arr = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == False
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6]) == False
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == True
    assert candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == False
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == False
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == False
    assert candidate(arr = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]) == True
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
    assert candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500]) == False
    assert candidate(arr = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491]) == False
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == False
    assert candidate(arr = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10]) == False
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == False
    assert candidate(arr = [1000, 1000, 1000, 999, 999, 998, 997, 996, 995, 994]) == False
    assert candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == False
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [-50, -50, -50, -50, -50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == True
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]) == True
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == False
    assert candidate(arr = [-10, -20, -30, -40, -50, -50, -40, -30, -20, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(arr = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 1]) == False
    assert candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False
    assert candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False
    assert candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984]) == False
    assert candidate(arr = [1000, -1000, 500, -500, 0, 0, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == False
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(arr = [-5, -5, -5, -5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(arr = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == False
    assert candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == False
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == True
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [10, 20, 10, 10, 30, 40, 40, 50, 50, 50]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
    assert candidate(arr = [10, 20, 20, 10, 30, 30, 30, 40, 40, 40, 40]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [-1, -2, -3, -4, -5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0]) == False
    assert candidate(arr = [0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6]) == False
    assert candidate(arr = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == False
    assert candidate(arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, 0, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [10, 20, 20, 10, 30, 40, 40, 40, 50, 50, 50, 50]) == False
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True


