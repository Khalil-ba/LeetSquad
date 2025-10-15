def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 6, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 6, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 3, 2, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 3, 2, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 11, 12],arr2 = [5, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 11, 12],arr2 = [5, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1],arr2 = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1],arr2 = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [4, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [4, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 20, 30],arr2 = [5, 15, 25, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 20, 30],arr2 = [5, 15, 25, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1],arr2 = [2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1],arr2 = [2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1],arr2 = [2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1],arr2 = [2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2000],arr2 = [1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2000],arr2 = [1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30],arr2 = [5, 15, 25, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30],arr2 = [5, 15, 25, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3],arr2 = [1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3],arr2 = [1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3],arr2 = [4, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3],arr2 = [4, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 4, 3, 5, 6, 7, 8],arr2 = [2, 3, 5, 7, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 4, 3, 5, 6, 7, 8],arr2 = [2, 3, 5, 7, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 3, 4, 5],arr2 = [2, 3, 4, 5, 6, 7, 8]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 3, 4, 5],arr2 = [2, 3, 4, 5, 6, 7, 8]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 3, 3, 3],arr2 = [2, 4, 6, 8, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 3, 3, 3],arr2 = [2, 4, 6, 8, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 2, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 2, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [2, 150, 250, 350]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [2, 150, 250, 350]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [3, 4, 5, 6, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [3, 4, 5, 6, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5, 11, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5, 11, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 9, 10, 9, 10],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 9, 10, 9, 10],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [50, 150, 250, 350]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [50, 150, 250, 350]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 10, 1],arr2 = [4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 10, 1],arr2 = [4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 2, 1, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 2, 1, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [15, 25, 35, 45, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [15, 25, 35, 45, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 3, 4, 5],arr2 = [2, 2, 2, 6, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 3, 4, 5],arr2 = [2, 2, 2, 6, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000000, 999999999, 999999998],arr2 = [1, 2, 3, 1000000001]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000000, 999999999, 999999998],arr2 = [1, 2, 3, 1000000001]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 100, 2, 101, 3, 102, 4],arr2 = [50, 51, 52, 53, 54]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 100, 2, 101, 3, 102, 4],arr2 = [50, 51, 52, 53, 54]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 5, 3, 8, 2],arr2 = [1, 4, 6, 9, 11]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 5, 3, 8, 2],arr2 = [1, 4, 6, 9, 11]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 9, 13, 17, 21],arr2 = [2, 6, 10, 14, 18, 22]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 9, 13, 17, 21],arr2 = [2, 6, 10, 14, 18, 22]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 10, 3, 4],arr2 = [5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 10, 3, 4],arr2 = [5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [3, 2, 1],arr2 = [4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [3, 2, 1],arr2 = [4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 10, 10, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 10, 10, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 5, 5, 5],arr2 = [2, 3, 4, 6, 7, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 5, 5, 5],arr2 = [2, 3, 4, 6, 7, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [1, 3, 5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [1, 3, 5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [6, 6, 6, 6, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [6, 6, 6, 6, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [8, 9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [8, 9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 25, 100, 150, 200],arr2 = [1, 20, 50, 125]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 25, 100, 150, 200],arr2 = [1, 20, 50, 125]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7, 8, 2, 10, 11, 12],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7, 8, 2, 10, 11, 12],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 6, 3, 4, 8, 9],arr2 = [2, 3, 7, 8, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 6, 3, 4, 8, 9],arr2 = [2, 3, 7, 8, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [3, 1, 1, 3],arr2 = [2, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [3, 1, 1, 3],arr2 = [2, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 1, 2, 3],arr2 = [2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 1, 2, 3],arr2 = [2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9, 11, 13],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9, 11, 13],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 3, 5, 7],arr2 = [2, 2, 4, 6, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 3, 5, 7],arr2 = [2, 2, 4, 6, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 9, 8, 7, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 9, 8, 7, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 3, 4, 4],arr2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 3, 4, 4],arr2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 100],arr2 = [2, 5, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 100],arr2 = [2, 5, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1000000000, 2, 999999999, 3],arr2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1000000000, 2, 999999999, 3],arr2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [3, 3, 3, 3, 3],arr2 = [1, 2, 2, 2, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [3, 3, 3, 3, 3],arr2 = [1, 2, 2, 2, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 14, 13, 8, 12],arr2 = [1, 4, 3, 9, 11, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 14, 13, 8, 12],arr2 = [1, 4, 3, 9, 11, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [150, 250, 350, 450, 550]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [150, 250, 350, 450, 550]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 10, 10, 1],arr2 = [2, 3, 4, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 10, 10, 1],arr2 = [2, 3, 4, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],arr2 = [2, 5, 8, 11, 14]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],arr2 = [2, 5, 8, 11, 14]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 100, 100],arr2 = [4, 5, 6, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 100, 100],arr2 = [4, 5, 6, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 3, 5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 3, 5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 150, 300, 250],arr2 = [120, 160, 180, 220, 260]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 150, 300, 250],arr2 = [120, 160, 180, 220, 260]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 5, 5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5, 6, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 5, 5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5, 6, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 3, 6, 7, 8, 9],arr2 = [1, 3, 2, 4, 5, 6, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 3, 6, 7, 8, 9],arr2 = [1, 3, 2, 4, 5, 6, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [6, 7, 8, 10, 9],arr2 = [2, 3, 5, 6, 11, 13, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [6, 7, 8, 10, 9],arr2 = [2, 3, 5, 6, 11, 13, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 90, 80, 70, 60],arr2 = [55, 65, 75, 85, 95, 105]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 90, 80, 70, 60],arr2 = [55, 65, 75, 85, 95, 105]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1000000000, 1, 1000000000, 1],arr2 = [2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1000000000, 1, 1000000000, 1],arr2 = [2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 50, 200, 250, 300],arr2 = [2, 20, 100, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 50, 200, 250, 300],arr2 = [2, 20, 100, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 12, 14, 16, 18],arr2 = [9, 11, 13, 15, 17]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 12, 14, 16, 18],arr2 = [9, 11, 13, 15, 17]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 2, 4, 5],arr2 = [1, 3, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 2, 4, 5],arr2 = [1, 3, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 4, 3, 5],arr2 = [2, 3, 4, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 4, 3, 5],arr2 = [2, 3, 4, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 20, 3, 40, 5],arr2 = [2, 19, 4, 39, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 20, 3, 40, 5],arr2 = [2, 19, 4, 39, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [500000000, 500000000, 500000000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [500000000, 500000000, 500000000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 5, 9, 13, 17],arr2 = [2, 6, 10, 14, 18]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 5, 9, 13, 17],arr2 = [2, 6, 10, 14, 18]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9],arr2 = [2, 5, 6, 8, 9, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9],arr2 = [2, 5, 6, 8, 9, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [2000, 1999, 1998, 1997, 1996],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [2000, 1999, 1998, 1997, 1996],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [25, 35, 45, 55, 65]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [25, 35, 45, 55, 65]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 100, 1000, 10000],arr2 = [5000, 500, 50, 5, 50000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 100, 1000, 10000],arr2 = [5000, 500, 50, 5, 50000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 3, 4, 2, 1],arr2 = [1, 2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 3, 4, 2, 1],arr2 = [1, 2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 9, 5, 7, 3],arr2 = [2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 9, 5, 7, 3],arr2 = [2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 25, 40, 50],arr2 = [15, 22, 28, 35, 45, 55]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 25, 40, 50],arr2 = [15, 22, 28, 35, 45, 55]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 20, 30, 100],arr2 = [2, 15, 25, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 20, 30, 100],arr2 = [2, 15, 25, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 2, 4, 3, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 2, 4, 3, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 0
    assert candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 6, 3, 3]) == -1
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9]) == 0
    assert candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [1, 3, 2, 4]) == 1
    assert candidate(arr1 = [10, 11, 12],arr2 = [5, 6, 7]) == 0
    assert candidate(arr1 = [1],arr2 = [2]) == 0
    assert candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [4, 3, 1]) == 2
    assert candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [1, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 0
    assert candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(arr1 = [1, 10, 20, 30],arr2 = [5, 15, 25, 35]) == 0
    assert candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5, 6]) == 3
    assert candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [5, 4, 3, 2, 1]) == 4
    assert candidate(arr1 = [1, 1, 1, 1],arr2 = [2, 2, 2, 2]) == -1
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10]) == 0
    assert candidate(arr1 = [1, 1, 1],arr2 = [2, 2, 2]) == -1
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 2, 2, 2, 2]) == -1
    assert candidate(arr1 = [1, 2000],arr2 = [1000]) == 0
    assert candidate(arr1 = [10, 20, 30],arr2 = [5, 15, 25, 35]) == 0
    assert candidate(arr1 = [1, 2, 3],arr2 = [1, 2, 3]) == 0
    assert candidate(arr1 = [1, 2, 3],arr2 = [4, 5, 6]) == 0
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [3, 4, 5]) == 3
    assert candidate(arr1 = [1, 2, 2, 4, 3, 5, 6, 7, 8],arr2 = [2, 3, 5, 7, 9]) == -1
    assert candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 2
    assert candidate(arr1 = [1, 2, 2, 3, 3, 4, 5],arr2 = [2, 3, 4, 5, 6, 7, 8]) == 5
    assert candidate(arr1 = [1, 3, 3, 3, 3],arr2 = [2, 4, 6, 8, 10]) == 3
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6]) == 4
    assert candidate(arr1 = [1, 3, 2, 5, 4],arr2 = [2, 2, 2, 2, 2, 2]) == -1
    assert candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [2, 150, 250, 350]) == 0
    assert candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [3, 4, 5, 6, 7]) == 3
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5, 11, 12]) == 4
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(arr1 = [1, 10, 9, 10, 9, 10],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(arr1 = [1, 100, 200, 300, 400],arr2 = [50, 150, 250, 350]) == 0
    assert candidate(arr1 = [1, 2, 3, 10, 1],arr2 = [4, 5, 6, 7, 8, 9]) == 2
    assert candidate(arr1 = [5, 2, 1, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [15, 25, 35, 45, 55]) == 0
    assert candidate(arr1 = [1, 3, 3, 4, 5],arr2 = [2, 2, 2, 6, 7]) == 1
    assert candidate(arr1 = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(arr1 = [1000000000, 999999999, 999999998],arr2 = [1, 2, 3, 1000000001]) == 2
    assert candidate(arr1 = [1, 100, 2, 101, 3, 102, 4],arr2 = [50, 51, 52, 53, 54]) == -1
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(arr1 = [10, 5, 3, 8, 2],arr2 = [1, 4, 6, 9, 11]) == 3
    assert candidate(arr1 = [1, 5, 9, 13, 17, 21],arr2 = [2, 6, 10, 14, 18, 22]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
    assert candidate(arr1 = [1, 2, 10, 3, 4],arr2 = [5, 6, 7, 8, 9]) == 3
    assert candidate(arr1 = [3, 2, 1],arr2 = [4, 5, 6]) == 2
    assert candidate(arr1 = [1, 3, 2, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 2
    assert candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(arr1 = [10, 10, 10, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 2, 2, 2, 2]) == -1
    assert candidate(arr1 = [1, 5, 5, 5, 5],arr2 = [2, 3, 4, 6, 7, 8]) == 3
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [1, 3, 5, 7, 9]) == 0
    assert candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [6, 6, 6, 6, 6]) == -1
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [8, 9, 10, 11, 12]) == 0
    assert candidate(arr1 = [5, 25, 100, 150, 200],arr2 = [1, 20, 50, 125]) == 0
    assert candidate(arr1 = [1, 5, 3, 6, 7, 8, 2, 10, 11, 12],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(arr1 = [1, 5, 3, 6, 7],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 1
    assert candidate(arr1 = [5, 6, 3, 4, 8, 9],arr2 = [2, 3, 7, 8, 11]) == -1
    assert candidate(arr1 = [10, 9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(arr1 = [3, 1, 1, 3],arr2 = [2, 4]) == -1
    assert candidate(arr1 = [1, 2, 3, 1, 2, 3],arr2 = [2, 3, 4, 5, 6]) == 3
    assert candidate(arr1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 5, 5, 5, 5]) == 0
    assert candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [2, 3, 4, 5]) == 3
    assert candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 9
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0
    assert candidate(arr1 = [5, 4, 3, 2, 1],arr2 = [6, 7, 8, 9, 10]) == 4
    assert candidate(arr1 = [5, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6]) == 0
    assert candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35]) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13],arr2 = [2, 4, 6, 8, 10, 12, 14]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(arr1 = [1, 3, 3, 5, 7],arr2 = [2, 2, 4, 6, 8]) == 1
    assert candidate(arr1 = [1, 9, 8, 7, 6],arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(arr1 = [1, 2, 2, 3, 3, 4, 4],arr2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(arr1 = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 100],arr2 = [2, 5, 8, 9]) == 0
    assert candidate(arr1 = [1, 1000000000, 2, 999999999, 3],arr2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 4
    assert candidate(arr1 = [3, 3, 3, 3, 3],arr2 = [1, 2, 2, 2, 4, 5]) == 4
    assert candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(arr1 = [5, 14, 13, 8, 12],arr2 = [1, 4, 3, 9, 11, 10]) == 3
    assert candidate(arr1 = [10, 9, 8, 7, 6],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55]) == 0
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [150, 250, 350, 450, 550]) == 0
    assert candidate(arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9
    assert candidate(arr1 = [1, 10, 10, 10, 1],arr2 = [2, 3, 4, 5, 6]) == 4
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(arr1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],arr2 = [2, 5, 8, 11, 14]) == -1
    assert candidate(arr1 = [1, 2, 3, 100, 100],arr2 = [4, 5, 6, 7]) == 1
    assert candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5]) == 4
    assert candidate(arr1 = [9, 8, 7, 6, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 3, 5, 7, 9]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0
    assert candidate(arr1 = [100, 200, 150, 300, 250],arr2 = [120, 160, 180, 220, 260]) == 2
    assert candidate(arr1 = [1, 2, 2, 2, 2],arr2 = [2, 3, 4, 5, 6]) == 3
    assert candidate(arr1 = [5, 5, 5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 5, 6, 7]) == 6
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(arr1 = [1, 10, 20, 30, 40],arr2 = [5, 15, 25, 35, 45]) == 0
    assert candidate(arr1 = [1, 5, 3, 6, 7, 8, 9],arr2 = [1, 3, 2, 4, 5, 6, 7]) == 1
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(arr1 = [1, 2, 2, 3, 4],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(arr1 = [6, 7, 8, 10, 9],arr2 = [2, 3, 5, 6, 11, 13, 15]) == 1
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(arr1 = [100, 90, 80, 70, 60],arr2 = [55, 65, 75, 85, 95, 105]) == 4
    assert candidate(arr1 = [1, 1000000000, 1, 1000000000, 1],arr2 = [2, 3, 4, 5]) == 4
    assert candidate(arr1 = [1, 50, 200, 250, 300],arr2 = [2, 20, 100, 225]) == 0
    assert candidate(arr1 = [10, 12, 14, 16, 18],arr2 = [9, 11, 13, 15, 17]) == 0
    assert candidate(arr1 = [1, 2, 2, 4, 5],arr2 = [1, 3, 5]) == 1
    assert candidate(arr1 = [1, 3, 2, 4, 3, 5],arr2 = [2, 3, 4, 5, 6]) == 4
    assert candidate(arr1 = [1, 20, 3, 40, 5],arr2 = [2, 19, 4, 39, 6]) == 2
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 6, 7, 8, 9, 10]) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [500000000, 500000000, 500000000]) == -1
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 11, 12, 13, 14, 15]) == 0
    assert candidate(arr1 = [1, 5, 9, 13, 17],arr2 = [2, 6, 10, 14, 18]) == 0
    assert candidate(arr1 = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9],arr2 = [2, 5, 6, 8, 9, 11]) == -1
    assert candidate(arr1 = [2000, 1999, 1998, 1997, 1996],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [25, 35, 45, 55, 65]) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(arr1 = [1, 10, 100, 1000, 10000],arr2 = [5000, 500, 50, 5, 50000]) == 0
    assert candidate(arr1 = [5, 3, 4, 2, 1],arr2 = [1, 2, 3, 4, 5, 6]) == 3
    assert candidate(arr1 = [1, 9, 5, 7, 3],arr2 = [2, 4, 6, 8, 10]) == 2
    assert candidate(arr1 = [10, 20, 30, 25, 40, 50],arr2 = [15, 22, 28, 35, 45, 55]) == 1
    assert candidate(arr1 = [1000000000, 1000000000, 1000000000],arr2 = [1, 2, 3]) == 2
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 0
    assert candidate(arr1 = [1, 3, 2, 4, 5, 6],arr2 = [2, 3, 4, 5, 6, 7]) == 2
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 0
    assert candidate(arr1 = [1, 3, 20, 30, 100],arr2 = [2, 15, 25, 90]) == 0
    assert candidate(arr1 = [1, 3, 2, 4, 3, 5, 4],arr2 = [2, 3, 4, 5, 6, 7]) == 5


