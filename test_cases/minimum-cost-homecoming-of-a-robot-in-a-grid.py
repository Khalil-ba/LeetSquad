def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 0],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 0],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 1],homePos = [1, 1],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 1],homePos = [1, 1],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 1],homePos = [2, 1],rowCosts = [3, 2, 1],colCosts = [4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 1],homePos = [2, 1],rowCosts = [3, 2, 1],colCosts = [4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [0, 0],rowCosts = [5],colCosts = [26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [0, 0],rowCosts = [5],colCosts = [26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1, 2],colCosts = [3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1, 2],colCosts = [3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4],colCosts = [5, 6, 7]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4],colCosts = [5, 6, 7]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 1],homePos = [3, 3],rowCosts = [3, 2, 1, 4],colCosts = [4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 1],homePos = [3, 3],rowCosts = [3, 2, 1, 4],colCosts = [4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 2],homePos = [2, 2],rowCosts = [10, 20, 30],colCosts = [5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 2],homePos = [2, 2],rowCosts = [10, 20, 30],colCosts = [5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 3],homePos = [1, 1],rowCosts = [1, 1, 1],colCosts = [1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 3],homePos = [1, 1],rowCosts = [1, 1, 1],colCosts = [1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 3],homePos = [1, 0],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 3],homePos = [1, 0],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 1],homePos = [2, 2],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 1],homePos = [2, 2],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 3],homePos = [7, 7],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 3],homePos = [7, 7],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [5, 4, 3, 2],colCosts = [1, 2, 3, 4, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [5, 4, 3, 2],colCosts = [1, 2, 3, 4, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [9, 0],homePos = [9, 9],rowCosts = [100],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [9, 0],homePos = [9, 9],rowCosts = [100],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [9, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [9, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [9, 0],homePos = [0, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [9, 0],homePos = [0, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 3],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 3],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 1],homePos = [2, 1],rowCosts = [1000, 2000, 3000, 4000],colCosts = [5000, 6000, 7000, 8000, 9000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 1],homePos = [2, 1],rowCosts = [1000, 2000, 3000, 4000],colCosts = [5000, 6000, 7000, 8000, 9000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 9],homePos = [0, 0],rowCosts = [1],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 9],homePos = [0, 0],rowCosts = [1],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 3],homePos = [4, 1],rowCosts = [3, 2, 1, 4, 5],colCosts = [6, 7, 8, 9]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 3],homePos = [4, 1],rowCosts = [3, 2, 1, 4, 5],colCosts = [6, 7, 8, 9]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [1, 2, 3, 4],colCosts = [4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [1, 2, 3, 4],colCosts = [4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1080: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 2],homePos = [2, 5],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 2],homePos = [2, 5],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [5, 10, 15, 20],colCosts = [10, 20, 30, 40]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [5, 10, 15, 20],colCosts = [10, 20, 30, 40]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [7, 2],rowCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [7, 2],rowCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 4],homePos = [2, 4],rowCosts = [100, 200, 300],colCosts = [100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 4],homePos = [2, 4],rowCosts = [100, 200, 300],colCosts = [100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300, 400, 500],colCosts = [100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300, 400, 500],colCosts = [100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 2],homePos = [4, 3],rowCosts = [100, 200, 300, 400, 500],colCosts = [10, 20, 30, 40]) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 2],homePos = [4, 3],rowCosts = [100, 200, 300, 400, 500],colCosts = [10, 20, 30, 40]) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 3],homePos = [3, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 6, 7, 8]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 3],homePos = [3, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 6, 7, 8]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3, 4, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3, 4, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 3],homePos = [4, 1],rowCosts = [2, 3, 5, 7, 11],colCosts = [13, 17, 19, 23]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 3],homePos = [4, 1],rowCosts = [2, 3, 5, 7, 11],colCosts = [13, 17, 19, 23]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 0],homePos = [0, 5],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 2, 3, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 0],homePos = [0, 5],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 2, 3, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10000, 9000, 8000, 7000],colCosts = [6000, 5000, 4000, 3000]) == 42000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10000, 9000, 8000, 7000],colCosts = [6000, 5000, 4000, 3000]) == 42000: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [6, 5, 4, 3, 2, 1]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [6, 5, 4, 3, 2, 1]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [2, 2, 2, 2, 2, 2],colCosts = [2, 2, 2, 2, 2, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [2, 2, 2, 2, 2, 2],colCosts = [2, 2, 2, 2, 2, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 3],homePos = [1, 1],rowCosts = [100, 200, 300, 400],colCosts = [400, 300, 200, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 3],homePos = [1, 1],rowCosts = [100, 200, 300, 400],colCosts = [400, 300, 200, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [7, 7],homePos = [2, 2],rowCosts = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [7, 7],homePos = [2, 2],rowCosts = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [9, 8, 7, 6, 5, 4],colCosts = [3, 2, 1, 4, 5, 6]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [9, 8, 7, 6, 5, 4],colCosts = [3, 2, 1, 4, 5, 6]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [4, 5],rowCosts = [10, 20, 30, 40, 50],colCosts = [5, 15, 25, 35, 45, 55]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [4, 5],rowCosts = [10, 20, 30, 40, 50],colCosts = [5, 15, 25, 35, 45, 55]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 4],homePos = [6, 6],rowCosts = [5, 1, 2, 3, 4, 3, 2, 1, 5, 10],colCosts = [10, 1, 2, 3, 4, 3, 2, 1, 5, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 4],homePos = [6, 6],rowCosts = [5, 1, 2, 3, 4, 3, 2, 1, 5, 10],colCosts = [10, 1, 2, 3, 4, 3, 2, 1, 5, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [40, 30, 20, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [40, 30, 20, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [5, 5],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [5, 5],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 0],homePos = [3, 2],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 0],homePos = [3, 2],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 2],homePos = [3, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 2],homePos = [3, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [10, 5],homePos = [10, 5],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [10, 5],homePos = [10, 5],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 0],homePos = [3, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 0],homePos = [3, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [1, 1],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [15, 25, 35, 45, 55, 65]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [1, 1],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [15, 25, 35, 45, 55, 65]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 0],homePos = [2, 4],rowCosts = [1, 2, 3],colCosts = [10, 20, 30, 40, 50]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 0],homePos = [2, 4],rowCosts = [1, 2, 3],colCosts = [10, 20, 30, 40, 50]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 1],homePos = [0, 3],rowCosts = [5, 10, 15, 20],colCosts = [1, 2, 3, 4]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 1],homePos = [0, 3],rowCosts = [5, 10, 15, 20],colCosts = [1, 2, 3, 4]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [5, 5],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [5, 5],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300],colCosts = [100, 200, 300]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300],colCosts = [100, 200, 300]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1000, 2000, 3000],colCosts = [100, 200, 300]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1000, 2000, 3000],colCosts = [100, 200, 300]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [5, 15, 25, 35, 45, 55]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [5, 15, 25, 35, 45, 55]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 3],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 3],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35, 45]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35, 45]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 4],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 4],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 4],homePos = [1, 1],rowCosts = [5, 10, 15, 20, 25],colCosts = [1, 2, 3, 4, 5]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 4],homePos = [1, 1],rowCosts = [5, 10, 15, 20, 25],colCosts = [1, 2, 3, 4, 5]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 2],homePos = [4, 2],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 2],homePos = [4, 2],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 0],homePos = [0, 4],rowCosts = [10, 20, 30, 40, 50],colCosts = [50, 40, 30, 20, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 0],homePos = [0, 4],rowCosts = [10, 20, 30, 40, 50],colCosts = [50, 40, 30, 20, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [99, 98, 97, 96, 95, 94]) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [99, 98, 97, 96, 95, 94]) == 490: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [3, 0],homePos = [0, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [3, 0],homePos = [0, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [4, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [4, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(startPos = [1, 5],homePos = [3, 2],rowCosts = [1, 2, 3, 4],colCosts = [5, 4, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startPos = [1, 5],homePos = [3, 2],rowCosts = [1, 2, 3, 4],colCosts = [5, 4, 3, 2, 1]) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22
    assert candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35]) == 105
    assert candidate(startPos = [1, 0],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 18
    assert candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 10, 1],colCosts = [1, 10, 1]) == 22
    assert candidate(startPos = [0, 0],homePos = [2, 2],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4
    assert candidate(startPos = [1, 1],homePos = [1, 1],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 0
    assert candidate(startPos = [2, 2],homePos = [0, 0],rowCosts = [1, 1, 1],colCosts = [1, 1, 1]) == 4
    assert candidate(startPos = [0, 1],homePos = [2, 1],rowCosts = [3, 2, 1],colCosts = [4, 5]) == 3
    assert candidate(startPos = [0, 0],homePos = [0, 0],rowCosts = [5],colCosts = [26]) == 0
    assert candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1, 2],colCosts = [3, 4]) == 0
    assert candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4],colCosts = [5, 6, 7]) == 17
    assert candidate(startPos = [0, 1],homePos = [3, 3],rowCosts = [3, 2, 1, 4],colCosts = [4, 3, 2, 1]) == 10
    assert candidate(startPos = [0, 2],homePos = [2, 2],rowCosts = [10, 20, 30],colCosts = [5, 5, 5]) == 50
    assert candidate(startPos = [2, 3],homePos = [1, 1],rowCosts = [1, 1, 1],colCosts = [1, 1, 1, 1]) == 3
    assert candidate(startPos = [2, 3],homePos = [1, 0],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 20
    assert candidate(startPos = [0, 1],homePos = [2, 2],rowCosts = [1, 2, 3],colCosts = [4, 5, 6]) == 11
    assert candidate(startPos = [3, 3],homePos = [7, 7],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [5, 4, 3, 2],colCosts = [1, 2, 3, 4, 5]) == 14
    assert candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 8
    assert candidate(startPos = [9, 0],homePos = [9, 9],rowCosts = [100],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540
    assert candidate(startPos = [0, 0],homePos = [9, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99
    assert candidate(startPos = [9, 0],homePos = [0, 9],rowCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99
    assert candidate(startPos = [2, 3],homePos = [2, 3],rowCosts = [5, 4, 3],colCosts = [8, 2, 6, 7]) == 0
    assert candidate(startPos = [5, 2],homePos = [0, 0],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 26
    assert candidate(startPos = [2, 1],homePos = [2, 1],rowCosts = [1000, 2000, 3000, 4000],colCosts = [5000, 6000, 7000, 8000, 9000]) == 0
    assert candidate(startPos = [0, 9],homePos = [0, 0],rowCosts = [1],colCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
    assert candidate(startPos = [2, 3],homePos = [4, 1],rowCosts = [3, 2, 1, 4, 5],colCosts = [6, 7, 8, 9]) == 24
    assert candidate(startPos = [1, 2],homePos = [3, 4],rowCosts = [1, 2, 3, 4],colCosts = [4, 3, 2, 1]) == 8
    assert candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1080
    assert candidate(startPos = [5, 2],homePos = [2, 5],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 180
    assert candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [5, 10, 15, 20],colCosts = [10, 20, 30, 40]) == 105
    assert candidate(startPos = [2, 2],homePos = [7, 2],rowCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 35
    assert candidate(startPos = [2, 4],homePos = [2, 4],rowCosts = [100, 200, 300],colCosts = [100, 200, 300, 400, 500]) == 0
    assert candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300, 400, 500],colCosts = [100, 200, 300, 400, 500]) == 0
    assert candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [60, 50, 40, 30, 20, 10]) == 400
    assert candidate(startPos = [1, 2],homePos = [4, 3],rowCosts = [100, 200, 300, 400, 500],colCosts = [10, 20, 30, 40]) == 1240
    assert candidate(startPos = [0, 3],homePos = [3, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 6, 7, 8]) == 108
    assert candidate(startPos = [4, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3, 4, 5]) == 110
    assert candidate(startPos = [1, 3],homePos = [4, 1],rowCosts = [2, 3, 5, 7, 11],colCosts = [13, 17, 19, 23]) == 59
    assert candidate(startPos = [5, 0],homePos = [0, 5],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 2, 3, 4, 5]) == 19
    assert candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 10
    assert candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10000, 9000, 8000, 7000],colCosts = [6000, 5000, 4000, 3000]) == 42000
    assert candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [6, 5, 4, 3, 2, 1]) == 170
    assert candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [2, 2, 2, 2, 2, 2],colCosts = [2, 2, 2, 2, 2, 2]) == 20
    assert candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
    assert candidate(startPos = [3, 3],homePos = [1, 1],rowCosts = [100, 200, 300, 400],colCosts = [400, 300, 200, 100]) == 1000
    assert candidate(startPos = [7, 7],homePos = [2, 2],rowCosts = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],colCosts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 60
    assert candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [9, 8, 7, 6, 5, 4],colCosts = [3, 2, 1, 4, 5, 6]) == 50
    assert candidate(startPos = [0, 0],homePos = [4, 5],rowCosts = [10, 20, 30, 40, 50],colCosts = [5, 15, 25, 35, 45, 55]) == 315
    assert candidate(startPos = [4, 4],homePos = [6, 6],rowCosts = [5, 1, 2, 3, 4, 3, 2, 1, 5, 10],colCosts = [10, 1, 2, 3, 4, 3, 2, 1, 5, 10]) == 10
    assert candidate(startPos = [3, 3],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [40, 30, 20, 10]) == 150
    assert candidate(startPos = [0, 0],homePos = [5, 5],rowCosts = [1, 2, 3, 4, 5, 6],colCosts = [6, 5, 4, 3, 2, 1]) == 35
    assert candidate(startPos = [0, 9],homePos = [9, 0],rowCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
    assert candidate(startPos = [3, 2],homePos = [0, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 5
    assert candidate(startPos = [1, 0],homePos = [3, 2],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4
    assert candidate(startPos = [1, 2],homePos = [3, 0],rowCosts = [1, 1, 1, 1],colCosts = [1, 1, 1]) == 4
    assert candidate(startPos = [0, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 24
    assert candidate(startPos = [10, 5],homePos = [10, 5],rowCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],colCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(startPos = [0, 0],homePos = [3, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1]) == 12
    assert candidate(startPos = [5, 5],homePos = [1, 1],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [15, 25, 35, 45, 55, 65]) == 300
    assert candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4
    assert candidate(startPos = [0, 4],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 64
    assert candidate(startPos = [2, 0],homePos = [2, 4],rowCosts = [1, 2, 3],colCosts = [10, 20, 30, 40, 50]) == 140
    assert candidate(startPos = [3, 1],homePos = [0, 3],rowCosts = [5, 10, 15, 20],colCosts = [1, 2, 3, 4]) == 37
    assert candidate(startPos = [5, 5],homePos = [5, 5],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [100, 200, 300],colCosts = [100, 200, 300]) == 0
    assert candidate(startPos = [2, 2],homePos = [2, 2],rowCosts = [1000, 2000, 3000],colCosts = [100, 200, 300]) == 0
    assert candidate(startPos = [5, 5],homePos = [0, 0],rowCosts = [10, 20, 30, 40, 50, 60],colCosts = [5, 15, 25, 35, 45, 55]) == 275
    assert candidate(startPos = [0, 3],homePos = [4, 0],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 26
    assert candidate(startPos = [3, 4],homePos = [0, 0],rowCosts = [10, 20, 30, 40],colCosts = [5, 15, 25, 35, 45]) == 140
    assert candidate(startPos = [4, 4],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 0
    assert candidate(startPos = [2, 2],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 4, 3, 2, 1]) == 12
    assert candidate(startPos = [4, 4],homePos = [1, 1],rowCosts = [5, 10, 15, 20, 25],colCosts = [1, 2, 3, 4, 5]) == 54
    assert candidate(startPos = [0, 2],homePos = [4, 2],rowCosts = [10, 20, 30, 40, 50],colCosts = [1, 2, 3]) == 140
    assert candidate(startPos = [4, 0],homePos = [0, 4],rowCosts = [10, 20, 30, 40, 50],colCosts = [50, 40, 30, 20, 10]) == 200
    assert candidate(startPos = [0, 5],homePos = [5, 0],rowCosts = [1, 1, 1, 1, 1, 1],colCosts = [99, 98, 97, 96, 95, 94]) == 490
    assert candidate(startPos = [1, 1],homePos = [3, 3],rowCosts = [1, 1, 1, 1, 1],colCosts = [1, 1, 1, 1, 1]) == 4
    assert candidate(startPos = [3, 0],homePos = [0, 3],rowCosts = [1, 2, 3, 4],colCosts = [1, 1, 1, 1, 1]) == 9
    assert candidate(startPos = [4, 0],homePos = [4, 4],rowCosts = [1, 2, 3, 4, 5],colCosts = [5, 10, 15, 20, 25]) == 70
    assert candidate(startPos = [1, 5],homePos = [3, 2],rowCosts = [1, 2, 3, 4],colCosts = [5, 4, 3, 2, 1]) == 13


