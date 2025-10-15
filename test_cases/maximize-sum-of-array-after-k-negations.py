def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 3],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 3],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50],k = 3) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50],k = 3) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50],k = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50],k = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -3, -1, 5, -4],k = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -3, -1, 5, -4],k = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 0, 2],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 0, 2],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3],k = 9) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3],k = 9) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 10) == 955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 10) == 955: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-7, 3, -5, 2, -1],k = 6) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-7, 3, -5, 2, -1],k = 6) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1],k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1],k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50],k = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50],k = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 50, -50, 25, -25],k = 10) == 298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 50, -50, 25, -25],k = 10) == 298: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100],k = 100) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100],k = 100) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 1) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 1) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6],k = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6],k = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50],k = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50],k = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 15) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 15) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1],k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1],k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, -2, 9, -4],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, -2, 9, -4],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9999) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9999) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 50, -50, 1],k = 10000) == 299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 50, -50, 1],k = 10000) == 299: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6],k = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6],k = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -2, 3, -4, 5, -6],k = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -2, 3, -4, 5, -6],k = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95],k = 15) == 970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95],k = 15) == 970: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40],k = 6) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40],k = 6) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 11) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 11) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],k = 9) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],k = 9) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 50, 25, -25, 12, -12, 6, -6, 3, -3],k = 12) == 186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 50, 25, -25, 12, -12, 6, -6, 3, -3],k = 12) == 186: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 3) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 3) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 1) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 1) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30],k = 6) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30],k = 6) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 7, -2, 1],k = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 7, -2, 1],k = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3],k = 7) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3],k = 7) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 20) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 20) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25],k = 11) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25],k = 11) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100],k = 10000) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100],k = 10000) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],k = 6) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],k = 6) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -10, 5],k = 3) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -10, 5],k = 3) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 50, -50, 25, -25],k = 7) == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 50, -50, 25, -25],k = 7) == 348: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -4, -5, -6],k = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -4, -5, -6],k = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],k = 9) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],k = 9) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 20) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 20) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 14) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 14) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-99, -98, -97, -96, -95],k = 10) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-99, -98, -97, -96, -95],k = 10) == 295: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],k = 7) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],k = 7) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100],k = 3) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100],k = 3) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],k = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],k = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 20) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 20) == 280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5],k = 6) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5],k = 6) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0],k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0],k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, -2, -3, -4],k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, -2, -3, -4],k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500],k = 2) == -1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500],k = 2) == -1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -50, 0, 50, 100],k = 3) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -50, 0, 50, 100],k = 3) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60],k = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60],k = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -50, -25, -12, -6, -3],k = 8) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -50, -25, -12, -6, -3],k = 8) == 196: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 0, 20, 10],k = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 0, 20, 10],k = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 20) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 20) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -100, -100, -100, -100],k = 10001) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -100, -100, -100, -100],k = 10001) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 6) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 6) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6],k = 20) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6],k = 20) == 374: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-5, -4, -3, -2, -1],k = 5) == 15
    assert candidate(nums = [0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [4, 2, 3],k = 1) == 5
    assert candidate(nums = [100, -100, 50, -50],k = 3) == 200
    assert candidate(nums = [1, 2, 3, 4],k = 2) == 10
    assert candidate(nums = [100, -100, 50, -50],k = 5) == 200
    assert candidate(nums = [2, -3, -1, 5, -4],k = 2) == 13
    assert candidate(nums = [3, -1, 0, 2],k = 3) == 6
    assert candidate(nums = [-1, -2, -3, -4],k = 2) == 4
    assert candidate(nums = [0, 0, 0, 0],k = 4) == 0
    assert candidate(nums = [1, 2, 3],k = 6) == 6
    assert candidate(nums = [-1, 0, 1],k = 1) == 2
    assert candidate(nums = [-1, -2, -3, -4],k = 4) == 10
    assert candidate(nums = [0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 13
    assert candidate(nums = [1, -1, 2, -2],k = 4) == 6
    assert candidate(nums = [1, 2, 3, 4],k = 4) == 10
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 10) == 20
    assert candidate(nums = [1, -1, 2, -2, 3, -3],k = 9) == 12
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 10) == 955
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],k = 5) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 53
    assert candidate(nums = [-7, 3, -5, 2, -1],k = 6) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 15) == 8
    assert candidate(nums = [-1, 1, -1, 1, -1],k = 8) == 3
    assert candidate(nums = [-10, 20, -30, 40, -50],k = 5) == 150
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 13
    assert candidate(nums = [99, -99, 50, -50, 25, -25],k = 10) == 298
    assert candidate(nums = [1, 2, 3, 4, 5],k = 20) == 15
    assert candidate(nums = [100, -100, 100, -100, 100],k = 100) == 500
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1) == 1300
    assert candidate(nums = [-1, -2, -3, -4],k = 10) == 10
    assert candidate(nums = [-10, -9, -8, -7, -6],k = 10) == 28
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 150
    assert candidate(nums = [-10, 20, -30, 40, -50],k = 15) == 150
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 250
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 15) == 550
    assert candidate(nums = [1, -1, 1, -1],k = 7) == 2
    assert candidate(nums = [5, -3, 8, -2, 9, -4],k = 3) == 31
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 10) == 13
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9999) == 8
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 15) == 20
    assert candidate(nums = [99, -99, 50, -50, 1],k = 10000) == 299
    assert candidate(nums = [1, -2, 3, -4, 5, -6],k = 5) == 21
    assert candidate(nums = [-1, -2, -3, -4],k = 3) == 8
    assert candidate(nums = [-1, 0, 1],k = 2) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 8
    assert candidate(nums = [0, 1, -2, 3, -4, 5, -6],k = 7) == 21
    assert candidate(nums = [1, -1, 1, -1, 1, -1],k = 100) == 4
    assert candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95],k = 15) == 970
    assert candidate(nums = [-10, -20, -30, -40],k = 6) == 100
    assert candidate(nums = [-1, 0, 1],k = 3) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 11) == 55
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],k = 9) == 45
    assert candidate(nums = [-50, 50, 25, -25, 12, -12, 6, -6, 3, -3],k = 12) == 186
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 7) == 55
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 130
    assert candidate(nums = [0, 0, 0, 0],k = 7) == 0
    assert candidate(nums = [-1, 1, -2, 2, -3, 3],k = 5) == 12
    assert candidate(nums = [2, 4, 6, 8, 10],k = 1) == 26
    assert candidate(nums = [-10, 10, -20, 20, -30, 30],k = 6) == 100
    assert candidate(nums = [5, -3, 7, -2, 1],k = 3) == 16
    assert candidate(nums = [0, 0, 0, 0, 0],k = 1000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 53
    assert candidate(nums = [-1, -2, -3, -4],k = 10) == 10
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == 55
    assert candidate(nums = [0, 0, 0, 0],k = 100) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 25
    assert candidate(nums = [100, 50, 25, 12, 6, 3],k = 7) == 190
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 20) == 110
    assert candidate(nums = [5, -5, 15, -15, 25, -25],k = 11) == 90
    assert candidate(nums = [100, 100, 100, 100, 100],k = 10000) == 500
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3],k = 7) == 12
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 6) == 100
    assert candidate(nums = [100, -50, 25, -10, 5],k = 3) == 180
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
    assert candidate(nums = [99, -99, 50, -50, 25, -25],k = 7) == 348
    assert candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 19
    assert candidate(nums = [1, -1, 1, -1, 1, -1],k = 10) == 4
    assert candidate(nums = [1, 2, 3, -4, -5, -6],k = 3) == 21
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 9) == 120
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 20) == 200
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
    assert candidate(nums = [0, 0, 0, 0, 0],k = 100) == 0
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 14) == 250
    assert candidate(nums = [-1, 0, 1],k = 5) == 2
    assert candidate(nums = [-99, -98, -97, -96, -95],k = 10) == 295
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 7) == 120
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 46
    assert candidate(nums = [100, 100, 100, 100, 100],k = 3) == 300
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],k = 15) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 100
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 20) == 280
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 10) == 55
    assert candidate(nums = [5, -5, 5, -5, 5, -5],k = 6) == 20
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0],k = 8) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
    assert candidate(nums = [5, -1, -2, -3, -4],k = 6) == 15
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
    assert candidate(nums = [-100, -200, -300, -400, -500],k = 2) == -1500
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
    assert candidate(nums = [-100, -50, 0, 50, 100],k = 3) == 300
    assert candidate(nums = [10, -20, 30, -40, 50, -60],k = 5) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 53
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10) == 10
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 3) == 90
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
    assert candidate(nums = [-100, -50, -25, -12, -6, -3],k = 8) == 196
    assert candidate(nums = [-10, -20, 0, 20, 10],k = 5) == 60
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 20) == 130
    assert candidate(nums = [-1, 0, 1],k = 1) == 2
    assert candidate(nums = [-100, -100, -100, -100, -100],k = 10001) == 500
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 6) == 130
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6],k = 20) == 374


