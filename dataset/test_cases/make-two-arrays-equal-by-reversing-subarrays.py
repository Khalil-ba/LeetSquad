def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = [4, 3, 2, 1],arr = [1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 3, 2, 1],arr = [1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 6, 7, 8],arr = [8, 7, 6, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 6, 7, 8],arr = [8, 7, 6, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1],arr = [1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1],arr = [1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7],arr = [7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7],arr = [7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 1000, 1000],arr = [1000, 1000, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 1000, 1000],arr = [1000, 1000, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40],arr = [40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40],arr = [40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3],arr = [3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3],arr = [3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 4, 3, 2, 1],arr = [1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 4, 3, 2, 1],arr = [1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30],arr = [30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30],arr = [30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 1, 3, 2],arr = [2, 1, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 1, 3, 2],arr = [2, 1, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 1, 1000],arr = [1, 1000, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 1, 1000],arr = [1, 1000, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3],arr = [2, 1, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3],arr = [2, 1, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 7, 9],arr = [3, 7, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 7, 9],arr = [3, 7, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 3, 1],arr = [1, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 3, 1],arr = [1, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4],arr = [2, 4, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4],arr = [2, 4, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3],arr = [3, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3],arr = [3, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 4, 4, 4],arr = [4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 4, 4, 4],arr = [4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 1, 1000, 1],arr = [1, 1000, 1, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 1, 1000, 1],arr = [1, 1000, 1, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 9, 8, 7],arr = [7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 9, 8, 7],arr = [7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 2],arr = [2, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 2],arr = [2, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3],arr = [4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3],arr = [4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [7],arr = [7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7],arr = [7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [999, 998, 997],arr = [997, 998, 999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [999, 998, 997],arr = [997, 998, 999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 6, 7],arr = [7, 6, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 6, 7],arr = [7, 6, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 2, 1, 3, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 2, 1, 3, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],arr = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],arr = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],arr = [991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],arr = [991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [500, 400, 300, 200, 100],arr = [100, 200, 300, 400, 500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [500, 400, 300, 200, 100],arr = [100, 200, 300, 400, 500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 2, 8, 4, 6, 5, 9, 7, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 2, 8, 4, 6, 5, 9, 7, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25],arr = [25, 20, 15, 10, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25],arr = [25, 20, 15, 10, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250],arr = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250],arr = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [999, 1000, 999, 1000, 999, 1000, 999, 1000],arr = [1000, 999, 1000, 999, 1000, 999, 1000, 999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [999, 1000, 999, 1000, 999, 1000, 999, 1000],arr = [1000, 999, 1000, 999, 1000, 999, 1000, 999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 1, 4, 3, 2],arr = [2, 3, 1, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 1, 4, 3, 2],arr = [2, 3, 1, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 3, 1, 4, 2],arr = [2, 1, 4, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 3, 1, 4, 2],arr = [2, 1, 4, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 1, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 1, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 3, 3, 3, 3],arr = [3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 3, 3, 3, 3],arr = [3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 500, 250, 125],arr = [125, 250, 500, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 500, 250, 125],arr = [125, 250, 500, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 2, 2, 2, 3, 3, 3],arr = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 2, 2, 2, 3, 3, 3],arr = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 200, 100, 200, 100],arr = [200, 100, 200, 100, 200]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 200, 100, 200, 100],arr = [200, 100, 200, 100, 200]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 200, 300, 400, 500],arr = [500, 400, 300, 200, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 200, 300, 400, 500],arr = [500, 400, 300, 200, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 500],arr = [500, 1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 500],arr = [500, 1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],arr = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],arr = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 8, 9, 10, 11],arr = [11, 10, 9, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 8, 9, 10, 11],arr = [11, 10, 9, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234],arr = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234],arr = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 999, 998, 997, 996],arr = [996, 997, 998, 999, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 999, 998, 997, 996],arr = [996, 997, 998, 999, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 100, 200, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 100, 200, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],arr = [50, 10, 30, 20, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],arr = [50, 10, 30, 20, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000, 999, 998, 997, 996, 995],arr = [995, 996, 997, 998, 999, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000, 999, 998, 997, 996, 995],arr = [995, 996, 997, 998, 999, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],arr = [4, 4, 3, 3, 4, 3, 2, 1, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],arr = [4, 4, 3, 3, 4, 3, 2, 1, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],arr = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],arr = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 3, 4, 1, 2],arr = [2, 1, 4, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 3, 4, 1, 2],arr = [2, 1, 4, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [10, 20, 30, 40, 50, 60, 70, 100, 90, 80]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [10, 20, 30, 40, 50, 60, 70, 100, 90, 80]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 2, 4, 5],arr = [2, 1, 4, 5, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 2, 4, 5],arr = [2, 1, 4, 5, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 3, 2, 1],arr = [1, 2, 3, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 3, 2, 1],arr = [1, 2, 3, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [200, 300, 100, 400, 500, 600],arr = [100, 200, 300, 400, 500, 600]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [200, 300, 100, 400, 500, 600],arr = [100, 200, 300, 400, 500, 600]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [9, 5, 3, 5, 2, 6, 9, 5, 1, 4, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [9, 5, 3, 5, 2, 6, 9, 5, 1, 4, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = [4, 3, 2, 1],arr = [1, 2, 3, 4]) == True
    assert candidate(target = [5, 6, 7, 8],arr = [8, 7, 6, 5]) == True
    assert candidate(target = [1, 1, 1, 1],arr = [1, 1, 1, 1]) == True
    assert candidate(target = [1, 3, 5, 7],arr = [7, 5, 3, 1]) == True
    assert candidate(target = [1000, 1000, 1000],arr = [1000, 1000, 1000]) == True
    assert candidate(target = [10, 20, 30, 40],arr = [40, 30, 20, 10]) == True
    assert candidate(target = [1, 2, 3],arr = [3, 2, 1]) == True
    assert candidate(target = [5, 4, 3, 2, 1],arr = [1, 2, 3, 4, 5]) == True
    assert candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True
    assert candidate(target = [10, 20, 30],arr = [30, 20, 10]) == True
    assert candidate(target = [5, 1, 3, 2],arr = [2, 1, 3, 5]) == True
    assert candidate(target = [1000, 1, 1000],arr = [1, 1000, 1000]) == True
    assert candidate(target = [1, 2, 2, 3],arr = [2, 1, 3, 2]) == True
    assert candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True
    assert candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True
    assert candidate(target = [3, 7, 9],arr = [3, 7, 11]) == False
    assert candidate(target = [5, 3, 1],arr = [1, 3, 5]) == True
    assert candidate(target = [1, 2, 3, 4],arr = [2, 4, 1, 3]) == True
    assert candidate(target = [1, 2, 2, 3],arr = [3, 2, 2, 1]) == True
    assert candidate(target = [4, 4, 4, 4],arr = [4, 4, 4, 4]) == True
    assert candidate(target = [1000, 1, 1000, 1],arr = [1, 1000, 1, 1000]) == True
    assert candidate(target = [10, 9, 8, 7],arr = [7, 8, 9, 10]) == True
    assert candidate(target = [1, 3, 2],arr = [2, 1, 3]) == True
    assert candidate(target = [1, 2, 3],arr = [4, 5, 6]) == False
    assert candidate(target = [7],arr = [7]) == True
    assert candidate(target = [999, 998, 997],arr = [997, 998, 999]) == True
    assert candidate(target = [5, 6, 7],arr = [7, 6, 5]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(target = [10, 20, 30, 40, 50],arr = [50, 40, 30, 20, 10]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 2, 1, 3, 1, 2]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],arr = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(target = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],arr = [991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [500, 400, 300, 200, 100],arr = [100, 200, 300, 400, 500]) == True
    assert candidate(target = [5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == True
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 2, 8, 4, 6, 5, 9, 7, 3, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == True
    assert candidate(target = [5, 10, 15, 20, 25],arr = [25, 20, 15, 10, 5]) == True
    assert candidate(target = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250],arr = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]) == True
    assert candidate(target = [1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 1]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [999, 1000, 999, 1000, 999, 1000, 999, 1000],arr = [1000, 999, 1000, 999, 1000, 999, 1000, 999]) == True
    assert candidate(target = [4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4]) == True
    assert candidate(target = [5, 1, 4, 3, 2],arr = [2, 3, 1, 5, 4]) == True
    assert candidate(target = [5, 3, 1, 4, 2],arr = [2, 1, 4, 3, 5]) == True
    assert candidate(target = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 1, 2, 3]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 1, 2]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == True
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(target = [3, 3, 3, 3, 3],arr = [3, 3, 3, 3, 3]) == True
    assert candidate(target = [1000, 500, 250, 125],arr = [125, 250, 500, 1000]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [1, 1, 1, 2, 2, 2, 3, 3, 3],arr = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == True
    assert candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
    assert candidate(target = [100, 200, 100, 200, 100],arr = [200, 100, 200, 100, 200]) == False
    assert candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [5, 5, 5, 5, 5, 5],arr = [5, 5, 5, 5, 5, 5]) == True
    assert candidate(target = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(target = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]) == True
    assert candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [100, 200, 300, 400, 500],arr = [500, 400, 300, 200, 100]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1]) == True
    assert candidate(target = [1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 500],arr = [500, 1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000]) == True
    assert candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],arr = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [7, 8, 9, 10, 11],arr = [11, 10, 9, 8, 7]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5],arr = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(target = [1, 3, 5, 7, 9],arr = [9, 7, 5, 3, 1]) == True
    assert candidate(target = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234],arr = [234, 234, 234, 234, 234, 234, 234, 234, 234, 234]) == True
    assert candidate(target = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(target = [1000, 999, 998, 997, 996],arr = [996, 997, 998, 999, 1000]) == True
    assert candidate(target = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == True
    assert candidate(target = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 100, 200, 300]) == True
    assert candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True
    assert candidate(target = [1, 2, 3, 4, 5],arr = [5, 4, 3, 2, 1]) == True
    assert candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]) == True
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]) == False
    assert candidate(target = [10, 20, 30, 40, 50],arr = [50, 10, 30, 20, 40]) == True
    assert candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True
    assert candidate(target = [1000, 999, 998, 997, 996, 995],arr = [995, 996, 997, 998, 999, 1000]) == True
    assert candidate(target = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],arr = [4, 4, 3, 3, 4, 3, 2, 1, 2, 4]) == True
    assert candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]) == False
    assert candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],arr = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
    assert candidate(target = [5, 3, 4, 1, 2],arr = [2, 1, 4, 3, 5]) == True
    assert candidate(target = [1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1]) == True
    assert candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr = [10, 20, 30, 40, 50, 60, 70, 100, 90, 80]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == False
    assert candidate(target = [1, 3, 2, 4, 5],arr = [2, 1, 4, 5, 3]) == True
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(target = [1, 2, 3, 4, 3, 2, 1],arr = [1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(target = [200, 300, 100, 400, 500, 600],arr = [100, 200, 300, 400, 500, 600]) == True
    assert candidate(target = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],arr = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]) == True
    assert candidate(target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],arr = [9, 5, 3, 5, 2, 6, 9, 5, 1, 4, 1, 3]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3, 4, 4],arr = [4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(target = [1, 1, 2, 2, 3, 3],arr = [3, 3, 2, 2, 1, 1]) == True
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True


