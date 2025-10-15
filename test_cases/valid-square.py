def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(p1 = [-1, -1],p2 = [-1, 1],p3 = [1, 1],p4 = [1, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1, -1],p2 = [-1, 1],p3 = [1, 1],p4 = [1, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [2, 2],p2 = [3, 3],p3 = [4, 4],p4 = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [2, 2],p2 = [3, 3],p3 = [4, 4],p4 = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 0],p2 = [-1, 0],p3 = [0, 1],p4 = [0, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 0],p2 = [-1, 0],p3 = [0, 1],p4 = [0, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [5, 6],p3 = [6, 6],p4 = [6, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [5, 6],p3 = [6, 6],p4 = [6, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 0],p3 = [1, 1],p4 = [0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 0],p3 = [1, 1],p4 = [0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 2],p3 = [3, 2],p4 = [2, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 2],p3 = [3, 2],p4 = [2, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 2],p4 = [2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 2],p4 = [2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 1],p4 = [1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 1],p4 = [1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [2, 0],p3 = [2, 2],p4 = [0, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [2, 0],p3 = [2, 2],p4 = [0, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [5, 0],p3 = [5, 5],p4 = [0, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [5, 0],p3 = [5, 5],p4 = [0, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 1],p3 = [1, 1],p4 = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 1],p3 = [1, 1],p4 = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [2, 2],p2 = [3, 3],p3 = [3, 2],p4 = [2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [2, 2],p2 = [3, 3],p3 = [3, 2],p4 = [2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 2],p4 = [2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 2],p4 = [2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 8],p4 = [10, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 8],p4 = [10, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 0],p3 = [0, 1],p4 = [1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 0],p3 = [0, 1],p4 = [1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, 2],p4 = [2, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, 2],p4 = [2, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [0, 0],p4 = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [0, 0],p4 = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [2, 2],p3 = [2, 3],p4 = [3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [2, 2],p3 = [2, 3],p4 = [3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-3, -3],p2 = [-2, -2],p3 = [-2, -1],p4 = [-1, -2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-3, -3],p2 = [-2, -2],p3 = [-2, -1],p4 = [-1, -2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 0],p4 = [1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 0],p4 = [1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1000, -1000],p2 = [-1000, 1000],p3 = [1000, 1000],p4 = [-1000, -1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1000, -1000],p2 = [-1000, 1000],p3 = [1000, 1000],p4 = [-1000, -1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-3, -3],p2 = [-3, 0],p3 = [0, -3],p4 = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-3, -3],p2 = [-3, 0],p3 = [0, -3],p4 = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-3, -3],p2 = [-3, -2],p3 = [-2, -2],p4 = [-2, -3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-3, -3],p2 = [-3, -2],p3 = [-2, -2],p4 = [-2, -3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [10, 0],p2 = [0, 10],p3 = [-10, 0],p4 = [0, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [10, 0],p2 = [0, 10],p3 = [-10, 0],p4 = [0, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-5, 2],p2 = [-2, 5],p3 = [1, 2],p4 = [-2, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-5, 2],p2 = [-2, 5],p3 = [1, 2],p4 = [-2, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 2],p2 = [3, 4],p3 = [2, 1],p4 = [0, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 2],p2 = [3, 4],p3 = [2, 1],p4 = [0, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-1, -1],p2 = [-1, 0],p3 = [0, -1],p4 = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1, -1],p2 = [-1, 0],p3 = [0, -1],p4 = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 1],p2 = [1, 0],p3 = [1, 2],p4 = [2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 1],p2 = [1, 0],p3 = [1, 2],p4 = [2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [2, 1],p3 = [2, 2],p4 = [1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [2, 1],p3 = [2, 2],p4 = [1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, -2],p4 = [2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, -2],p4 = [2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-1, -1],p2 = [0, 0],p3 = [1, -1],p4 = [0, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1, -1],p2 = [0, 0],p3 = [1, -1],p4 = [0, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [6, 5],p3 = [6, 6],p4 = [5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [6, 5],p3 = [6, 6],p4 = [5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [7, 7],p2 = [7, 9],p3 = [9, 7],p4 = [9, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [7, 7],p2 = [7, 9],p3 = [9, 7],p4 = [9, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 10],p4 = [10, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 10],p4 = [10, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 3],p3 = [3, 3],p4 = [3, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 3],p3 = [3, 3],p4 = [3, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 5],p3 = [5, 5],p4 = [5, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 5],p3 = [5, 5],p4 = [5, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 0],p4 = [2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 0],p4 = [2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 2],p4 = [2, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 2],p4 = [2, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [10, 10],p2 = [14, 14],p3 = [14, 10],p4 = [10, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [10, 10],p2 = [14, 14],p3 = [14, 10],p4 = [10, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-100, -100],p2 = [-99, -99],p3 = [-99, -100],p4 = [-100, -99]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-100, -100],p2 = [-99, -99],p3 = [-99, -100],p4 = [-100, -99]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 0],p2 = [0, 1],p3 = [1, 2],p4 = [2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 0],p2 = [0, 1],p3 = [1, 2],p4 = [2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-1000, -1000],p2 = [-999, -999],p3 = [-999, -1000],p4 = [-1000, -999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1000, -1000],p2 = [-999, -999],p3 = [-999, -1000],p4 = [-1000, -999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-10000, -10000],p2 = [-10000, -9999],p3 = [-9999, -10000],p4 = [-9999, -9999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-10000, -10000],p2 = [-10000, -9999],p3 = [-9999, -10000],p4 = [-9999, -9999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [6, 6],p3 = [7, 7],p4 = [8, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [6, 6],p3 = [7, 7],p4 = [8, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [3, 3],p2 = [6, 6],p3 = [6, 3],p4 = [3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [3, 3],p2 = [6, 6],p3 = [6, 3],p4 = [3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-5, -5],p2 = [-10, -5],p3 = [-10, -10],p4 = [-5, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-5, -5],p2 = [-10, -5],p3 = [-10, -10],p4 = [-5, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [3, 3],p2 = [6, 3],p3 = [6, 6],p4 = [3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [3, 3],p2 = [6, 3],p3 = [6, 6],p4 = [3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [1, 1],p4 = [2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [1, 1],p4 = [2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [10, 10],p2 = [10, 20],p3 = [20, 10],p4 = [20, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [10, 10],p2 = [10, 20],p3 = [20, 10],p4 = [20, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 3],p4 = [3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 3],p4 = [3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [1, -1],p4 = [-1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [1, -1],p4 = [-1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [6, 6],p3 = [6, 5],p4 = [5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [6, 6],p3 = [6, 5],p4 = [5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 2],p4 = [4, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 2],p4 = [4, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 0],p4 = [2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 0],p4 = [2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-2, -2],p2 = [-2, -3],p3 = [-3, -3],p4 = [-3, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-2, -2],p2 = [-2, -3],p3 = [-3, -3],p4 = [-3, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [4, 5],p3 = [5, 4],p4 = [8, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [4, 5],p3 = [5, 4],p4 = [8, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [100, 100],p2 = [101, 101],p3 = [101, 100],p4 = [100, 101]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [100, 100],p2 = [101, 101],p3 = [101, 100],p4 = [100, 101]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 10000],p3 = [10000, 0],p4 = [10000, 10000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 10000],p3 = [10000, 0],p4 = [10000, 10000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 5],p4 = [10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 5],p4 = [10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1000, 1000],p2 = [1000, 2000],p3 = [2000, 2000],p4 = [2000, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1000, 1000],p2 = [1000, 2000],p3 = [2000, 2000],p4 = [2000, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [3, 4],p2 = [6, 8],p3 = [9, 5],p4 = [6, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [3, 4],p2 = [6, 8],p3 = [9, 5],p4 = [6, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [-2, -1],p4 = [-1, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [-2, -1],p4 = [-1, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [5, 5],p2 = [8, 5],p3 = [8, 8],p4 = [5, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [5, 5],p2 = [8, 5],p3 = [8, 8],p4 = [5, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [10000, 10000],p2 = [10001, 10001],p3 = [10001, 10000],p4 = [10000, 9999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [10000, 10000],p2 = [10001, 10001],p3 = [10001, 10000],p4 = [10000, 9999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [-5, 5],p2 = [-4, 4],p3 = [-4, 5],p4 = [-5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [-5, 5],p2 = [-4, 4],p3 = [-4, 5],p4 = [-5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(p1 = [0, 0],p2 = [0, 4],p3 = [4, 4],p4 = [4, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p1 = [0, 0],p2 = [0, 4],p3 = [4, 4],p4 = [4, 0]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(p1 = [-1, -1],p2 = [-1, 1],p3 = [1, 1],p4 = [1, -1]) == True
    assert candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False
    assert candidate(p1 = [2, 2],p2 = [3, 3],p3 = [4, 4],p4 = [5, 5]) == False
    assert candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False
    assert candidate(p1 = [1, 0],p2 = [-1, 0],p3 = [0, 1],p4 = [0, -1]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 12]) == False
    assert candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 2]) == True
    assert candidate(p1 = [5, 5],p2 = [5, 6],p3 = [6, 6],p4 = [6, 5]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 0],p3 = [1, 1],p4 = [0, 1]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 2],p3 = [3, 2],p4 = [2, 0]) == False
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 2],p4 = [2, 1]) == False
    assert candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 5]) == False
    assert candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 1],p4 = [1, 0]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, 1]) == True
    assert candidate(p1 = [0, 0],p2 = [2, 0],p3 = [2, 2],p4 = [0, 2]) == True
    assert candidate(p1 = [0, 0],p2 = [5, 0],p3 = [5, 5],p4 = [0, 5]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 1],p3 = [1, 1],p4 = [1, 1]) == False
    assert candidate(p1 = [2, 2],p2 = [3, 3],p3 = [3, 2],p4 = [2, 3]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 2],p4 = [2, 1]) == True
    assert candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 8],p4 = [10, 11]) == False
    assert candidate(p1 = [0, 0],p2 = [1, 0],p3 = [0, 1],p4 = [1, 1]) == True
    assert candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, 2],p4 = [2, -2]) == True
    assert candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True
    assert candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [0, 0],p4 = [2, 2]) == False
    assert candidate(p1 = [1, 1],p2 = [2, 2],p3 = [2, 3],p4 = [3, 2]) == False
    assert candidate(p1 = [-3, -3],p2 = [-2, -2],p3 = [-2, -1],p4 = [-1, -2]) == False
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 0],p4 = [1, 2]) == False
    assert candidate(p1 = [1000, -1000],p2 = [-1000, 1000],p3 = [1000, 1000],p4 = [-1000, -1000]) == True
    assert candidate(p1 = [-3, -3],p2 = [-3, 0],p3 = [0, -3],p4 = [0, 0]) == True
    assert candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True
    assert candidate(p1 = [-3, -3],p2 = [-3, -2],p3 = [-2, -2],p4 = [-2, -3]) == True
    assert candidate(p1 = [10, 0],p2 = [0, 10],p3 = [-10, 0],p4 = [0, -10]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True
    assert candidate(p1 = [-5, 2],p2 = [-2, 5],p3 = [1, 2],p4 = [-2, -1]) == True
    assert candidate(p1 = [1, 2],p2 = [3, 4],p3 = [2, 1],p4 = [0, -1]) == False
    assert candidate(p1 = [-1, -1],p2 = [-1, 0],p3 = [0, -1],p4 = [0, 0]) == True
    assert candidate(p1 = [0, 1],p2 = [1, 0],p3 = [1, 2],p4 = [2, 1]) == True
    assert candidate(p1 = [1, 1],p2 = [2, 1],p3 = [2, 2],p4 = [1, 2]) == True
    assert candidate(p1 = [-2, -2],p2 = [-2, 2],p3 = [2, -2],p4 = [2, 2]) == True
    assert candidate(p1 = [1, 0],p2 = [0, 1],p3 = [-1, 0],p4 = [0, -1]) == True
    assert candidate(p1 = [-1, -1],p2 = [0, 0],p3 = [1, -1],p4 = [0, -2]) == True
    assert candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True
    assert candidate(p1 = [5, 5],p2 = [6, 5],p3 = [6, 6],p4 = [5, 6]) == True
    assert candidate(p1 = [7, 7],p2 = [7, 9],p3 = [9, 7],p4 = [9, 9]) == True
    assert candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 10],p4 = [10, 5]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 3],p3 = [3, 3],p4 = [3, 0]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 2],p3 = [2, 1],p4 = [2, 3]) == False
    assert candidate(p1 = [0, 0],p2 = [0, 5],p3 = [5, 5],p4 = [5, 0]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 0],p4 = [2, 2]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 2],p3 = [2, 2],p4 = [2, 0]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False
    assert candidate(p1 = [10, 10],p2 = [14, 14],p3 = [14, 10],p4 = [10, 14]) == True
    assert candidate(p1 = [-100, -100],p2 = [-99, -99],p3 = [-99, -100],p4 = [-100, -99]) == True
    assert candidate(p1 = [1, 0],p2 = [0, 1],p3 = [1, 2],p4 = [2, 1]) == True
    assert candidate(p1 = [-1000, -1000],p2 = [-999, -999],p3 = [-999, -1000],p4 = [-1000, -999]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 1],p4 = [3, 3]) == True
    assert candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False
    assert candidate(p1 = [0, 0],p2 = [0, 0],p3 = [0, 0],p4 = [0, 0]) == False
    assert candidate(p1 = [-10000, -10000],p2 = [-10000, -9999],p3 = [-9999, -10000],p4 = [-9999, -9999]) == True
    assert candidate(p1 = [5, 5],p2 = [6, 6],p3 = [7, 7],p4 = [8, 8]) == False
    assert candidate(p1 = [3, 3],p2 = [6, 6],p3 = [6, 3],p4 = [3, 6]) == True
    assert candidate(p1 = [-5, -5],p2 = [-10, -5],p3 = [-10, -10],p4 = [-5, -10]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [1, 0],p4 = [0, -1]) == False
    assert candidate(p1 = [3, 3],p2 = [6, 3],p3 = [6, 6],p4 = [3, 6]) == True
    assert candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [1, 1],p4 = [2, 2]) == False
    assert candidate(p1 = [10, 10],p2 = [10, 20],p3 = [20, 10],p4 = [20, 20]) == True
    assert candidate(p1 = [1, 1],p2 = [1, 3],p3 = [3, 3],p4 = [3, 1]) == True
    assert candidate(p1 = [-1, -1],p2 = [1, 1],p3 = [1, -1],p4 = [-1, 1]) == True
    assert candidate(p1 = [1000, 1000],p2 = [1001, 1001],p3 = [1001, 1000],p4 = [1000, 1001]) == True
    assert candidate(p1 = [0, 0],p2 = [1, 1],p3 = [2, 2],p4 = [3, 3]) == False
    assert candidate(p1 = [5, 5],p2 = [6, 6],p3 = [6, 5],p4 = [5, 6]) == True
    assert candidate(p1 = [1, 2],p2 = [3, 4],p3 = [5, 6],p4 = [7, 8]) == False
    assert candidate(p1 = [1, 2],p2 = [4, 5],p3 = [7, 2],p4 = [4, -1]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 1],p3 = [1, 0],p4 = [2, 1]) == False
    assert candidate(p1 = [-2, -2],p2 = [-2, -3],p3 = [-3, -3],p4 = [-3, -2]) == True
    assert candidate(p1 = [1, 1],p2 = [4, 5],p3 = [5, 4],p4 = [8, 8]) == False
    assert candidate(p1 = [100, 100],p2 = [101, 101],p3 = [101, 100],p4 = [100, 101]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 10000],p3 = [10000, 0],p4 = [10000, 10000]) == True
    assert candidate(p1 = [5, 5],p2 = [5, 10],p3 = [10, 5],p4 = [10, 10]) == True
    assert candidate(p1 = [1000, 1000],p2 = [1000, 2000],p3 = [2000, 2000],p4 = [2000, 1000]) == True
    assert candidate(p1 = [1, 1],p2 = [2, 2],p3 = [3, 3],p4 = [4, 4]) == False
    assert candidate(p1 = [0, 1],p2 = [1, 0],p3 = [0, -1],p4 = [-1, 0]) == True
    assert candidate(p1 = [3, 4],p2 = [6, 8],p3 = [9, 5],p4 = [6, 1]) == False
    assert candidate(p1 = [-2, -2],p2 = [-1, -1],p3 = [-2, -1],p4 = [-1, -2]) == True
    assert candidate(p1 = [5, 5],p2 = [8, 5],p3 = [8, 8],p4 = [5, 8]) == True
    assert candidate(p1 = [10000, 10000],p2 = [10001, 10001],p3 = [10001, 10000],p4 = [10000, 9999]) == False
    assert candidate(p1 = [-5, 5],p2 = [-4, 4],p3 = [-4, 5],p4 = [-5, 4]) == True
    assert candidate(p1 = [0, 0],p2 = [0, 4],p3 = [4, 4],p4 = [4, 0]) == True


