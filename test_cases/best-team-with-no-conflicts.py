def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(scores = [1000000, 999999, 999998],ages = [1, 2, 3]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000000, 999999, 999998],ages = [1, 2, 3]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [50, 50, 50, 50],ages = [1, 2, 3, 4]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [50, 50, 50, 50],ages = [1, 2, 3, 4]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 22, 35, 47, 55, 65],ages = [16, 19, 22, 25, 28, 31]) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 22, 35, 47, 55, 65],ages = [16, 19, 22, 25, 28, 31]) == 234: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 5, 5, 5],ages = [1, 2, 3, 4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 5, 5, 5],ages = [1, 2, 3, 4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100000, 100000, 100000],ages = [1000, 1000, 1000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100000, 100000, 100000],ages = [1000, 1000, 1000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 300, 400],ages = [4, 3, 2, 1]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 300, 400],ages = [4, 3, 2, 1]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 5, 6, 5],ages = [2, 1, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 5, 6, 5],ages = [2, 1, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 5],ages = [8, 9, 10, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 5],ages = [8, 9, 10, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 9, 8, 7],ages = [1, 2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 9, 8, 7],ages = [1, 2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 3, 7, 5, 2],ages = [5, 4, 8, 5, 2]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 3, 7, 5, 2],ages = [5, 4, 8, 5, 2]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000000, 1000000, 1000000],ages = [1, 1, 1]) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000000, 1000000, 1000000],ages = [1, 1, 1]) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 5, 10, 15],ages = [1, 2, 3, 4, 5]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 5, 10, 15],ages = [1, 2, 3, 4, 5]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 2, 1],ages = [3, 1, 1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 2, 1],ages = [3, 1, 1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60],ages = [18, 17, 16, 15, 14]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60],ages = [18, 17, 16, 15, 14]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [90, 85, 90, 100, 105, 110, 105, 115, 120],ages = [25, 30, 25, 30, 35, 40, 45, 50, 55]) == 730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [90, 85, 90, 100, 105, 110, 105, 115, 120],ages = [25, 30, 25, 30, 35, 40, 45, 50, 55]) == 730: {e}')
    
    total += 1
    try:
        result = candidate(scores = [2, 5, 3, 1, 4],ages = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [2, 5, 3, 1, 4],ages = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 30, 20, 30, 20],ages = [2, 2, 3, 3, 4]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 30, 20, 30, 20],ages = [2, 2, 3, 3, 4]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 5, 7, 1, 9, 6, 8, 3, 4, 2],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 5, 7, 1, 9, 6, 8, 3, 4, 2],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 20, 10, 40, 50],ages = [1, 2, 3, 1, 2, 3, 4]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 20, 10, 40, 50],ages = [1, 2, 3, 1, 2, 3, 4]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [25, 30, 5, 50, 40, 60, 70, 10, 80, 90],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [25, 30, 5, 50, 40, 60, 70, 10, 80, 90],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 10, 4, 3, 8, 9],ages = [4, 1, 2, 4, 3, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 10, 4, 3, 8, 9],ages = [4, 1, 2, 4, 3, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],ages = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],ages = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40],ages = [1, 3, 2, 5, 4, 7, 6, 8]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40],ages = [1, 3, 2, 5, 4, 7, 6, 8]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(scores = [40, 20, 30, 10, 50],ages = [2, 1, 3, 4, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [40, 20, 30, 10, 50],ages = [2, 1, 3, 4, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 605: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 25, 40],ages = [4, 3, 5, 2, 6]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 25, 40],ages = [4, 3, 5, 2, 6]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 30, 25, 20, 40, 35, 30, 45, 50, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 30, 25, 20, 40, 35, 30, 45, 50, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 245: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 6, 5, 7, 3, 8],ages = [4, 3, 2, 4, 1, 5]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 6, 5, 7, 3, 8],ages = [4, 3, 2, 4, 1, 5]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(scores = [8, 5, 6, 10, 7, 9, 4, 2, 11, 3],ages = [8, 6, 6, 9, 7, 8, 5, 4, 10, 3]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [8, 5, 6, 10, 7, 9, 4, 2, 11, 3],ages = [8, 6, 6, 9, 7, 8, 5, 4, 10, 3]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000, 500, 250, 750, 100],ages = [20, 25, 30, 35, 40]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000, 500, 250, 750, 100],ages = [20, 25, 30, 35, 40]) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 1, 3, 2, 5],ages = [2, 1, 2, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 1, 3, 2, 5],ages = [2, 1, 2, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50],ages = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50],ages = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],ages = [1, 2, 1, 3, 2, 4, 3, 5, 4, 5]) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],ages = [1, 2, 1, 3, 2, 4, 3, 5, 4, 5]) == 310: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 9, 2, 5, 3, 7, 1, 8, 6, 4],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 9, 2, 5, 3, 7, 1, 8, 6, 4],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000000, 100000, 10000, 1000, 100, 10, 1],ages = [1, 2, 3, 4, 5, 6, 7]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000000, 100000, 10000, 1000, 100, 10, 1],ages = [1, 2, 3, 4, 5, 6, 7]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50],ages = [3, 2, 1, 2, 3]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50],ages = [3, 2, 1, 2, 3]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(scores = [9, 2, 8, 5, 7, 6, 3, 4, 1, 10],ages = [4, 1, 6, 3, 5, 4, 2, 3, 1, 7]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [9, 2, 8, 5, 7, 6, 3, 4, 1, 10],ages = [4, 1, 6, 3, 5, 4, 2, 3, 1, 7]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 300, 400, 500],ages = [5, 4, 3, 2, 1]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 300, 400, 500],ages = [5, 4, 3, 2, 1]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 300, 200, 100],ages = [1, 2, 3, 4, 5]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 300, 200, 100],ages = [1, 2, 3, 4, 5]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(scores = [9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 5, 6, 5, 7, 8, 6, 9],ages = [2, 1, 2, 1, 3, 4, 3, 5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 5, 6, 5, 7, 8, 6, 9],ages = [2, 1, 2, 1, 3, 4, 3, 5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 30, 10, 40, 50],ages = [10, 10, 10, 10, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 30, 10, 40, 50],ages = [10, 10, 10, 10, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [9, 2, 8, 8, 8, 2, 1, 1, 1, 4],ages = [6, 2, 4, 7, 7, 2, 2, 2, 4, 3]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [9, 2, 8, 8, 8, 2, 1, 1, 1, 4],ages = [6, 2, 4, 7, 7, 2, 2, 2, 4, 3]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(scores = [8, 2, 7, 5, 4, 3, 9],ages = [2, 3, 1, 2, 3, 4, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [8, 2, 7, 5, 4, 3, 9],ages = [2, 3, 1, 2, 3, 4, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],ages = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],ages = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(scores = [15, 20, 5, 10, 25, 30],ages = [5, 5, 2, 3, 5, 5]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [15, 20, 5, 10, 25, 30],ages = [5, 5, 2, 3, 5, 5]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 10, 15, 20, 25, 30, 35],ages = [20, 20, 20, 20, 20, 20, 20]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 10, 15, 20, 25, 30, 35],ages = [20, 20, 20, 20, 20, 20, 20]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(scores = [8, 6, 7, 5, 3, 0, 9],ages = [1, 2, 2, 3, 3, 3, 4]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [8, 6, 7, 5, 3, 0, 9],ages = [1, 2, 2, 3, 3, 3, 4]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 10, 2, 1, 5, 7, 8, 6, 4, 9],ages = [1, 3, 2, 4, 2, 2, 3, 2, 2, 1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 10, 2, 1, 5, 7, 8, 6, 4, 9],ages = [1, 3, 2, 4, 2, 2, 3, 2, 2, 1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(scores = [50, 40, 30, 20, 10, 100, 90, 80, 70, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [50, 40, 30, 20, 10, 100, 90, 80, 70, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(scores = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 20, 10, 30, 30, 40, 40],ages = [1, 1, 2, 2, 3, 3, 4, 4]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 20, 10, 30, 30, 40, 40],ages = [1, 1, 2, 2, 3, 3, 4, 4]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 20, 10, 30],ages = [1, 2, 3, 4, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 20, 10, 30],ages = [1, 2, 3, 4, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000, 1000, 1000, 1000, 1000],ages = [1, 1, 1, 1, 1]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000, 1000, 1000, 1000, 1000],ages = [1, 1, 1, 1, 1]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55],ages = [3, 1, 2, 4, 5, 1, 2, 3, 4, 5]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55],ages = [3, 1, 2, 4, 5, 1, 2, 3, 4, 5]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(scores = [50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 150, 100, 50, 250],ages = [5, 4, 3, 2, 1, 6]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 150, 100, 50, 250],ages = [5, 4, 3, 2, 1, 6]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 1, 2],ages = [1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 1, 2],ages = [1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 1, 6, 2, 5, 3],ages = [2, 1, 3, 1, 2, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 1, 6, 2, 5, 3],ages = [2, 1, 3, 1, 2, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],ages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],ages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(scores = [15, 30, 10, 20, 50],ages = [5, 10, 15, 20, 25]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [15, 30, 10, 20, 50],ages = [5, 10, 15, 20, 25]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(scores = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],ages = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],ages = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000, 500, 200, 1000, 1000, 500, 200],ages = [2, 1, 3, 2, 3, 1, 3]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000, 500, 200, 1000, 1000, 500, 200],ages = [2, 1, 3, 2, 3, 1, 3]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 200, 300, 400, 500, 150, 250, 350, 450, 550],ages = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == 1750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 200, 300, 400, 500, 150, 250, 350, 450, 550],ages = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == 1750: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50],ages = [1, 3, 2, 5, 4]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50],ages = [1, 3, 2, 5, 4]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(scores = [4, 10, 10, 6, 7, 1, 9],ages = [4, 1, 4, 2, 2, 3, 6]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [4, 10, 10, 6, 7, 1, 9],ages = [4, 1, 4, 2, 2, 3, 6]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5],ages = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5],ages = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(scores = [5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(scores = [100, 90, 80, 70, 60],ages = [5, 4, 3, 2, 1]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [100, 90, 80, 70, 60],ages = [5, 4, 3, 2, 1]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(scores = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1998046
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1998046: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(scores = [1000000, 999999, 999998],ages = [1, 2, 3]) == 1000000
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(scores = [50, 50, 50, 50],ages = [1, 2, 3, 4]) == 200
    assert candidate(scores = [10, 22, 35, 47, 55, 65],ages = [16, 19, 22, 25, 28, 31]) == 234
    assert candidate(scores = [5, 5, 5, 5],ages = [1, 2, 3, 4]) == 20
    assert candidate(scores = [1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1]) == 5
    assert candidate(scores = [100000, 100000, 100000],ages = [1000, 1000, 1000]) == 300000
    assert candidate(scores = [100, 200, 300, 400],ages = [4, 3, 2, 1]) == 400
    assert candidate(scores = [4, 5, 6, 5],ages = [2, 1, 2, 1]) == 16
    assert candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(scores = [1, 2, 3, 5],ages = [8, 9, 10, 1]) == 6
    assert candidate(scores = [10, 9, 8, 7],ages = [1, 2, 3, 4]) == 10
    assert candidate(scores = [5, 3, 7, 5, 2],ages = [5, 4, 8, 5, 2]) == 22
    assert candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(scores = [1000000, 1000000, 1000000],ages = [1, 1, 1]) == 3000000
    assert candidate(scores = [1, 3, 5, 10, 15],ages = [1, 2, 3, 4, 5]) == 34
    assert candidate(scores = [1, 2, 2, 1],ages = [3, 1, 1, 3]) == 4
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
    assert candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
    assert candidate(scores = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150
    assert candidate(scores = [100, 90, 80, 70, 60],ages = [18, 17, 16, 15, 14]) == 400
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550
    assert candidate(scores = [90, 85, 90, 100, 105, 110, 105, 115, 120],ages = [25, 30, 25, 30, 35, 40, 45, 50, 55]) == 730
    assert candidate(scores = [2, 5, 3, 1, 4],ages = [1, 2, 3, 4, 5]) == 9
    assert candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(scores = [20, 30, 20, 30, 20],ages = [2, 2, 3, 3, 4]) == 80
    assert candidate(scores = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 36
    assert candidate(scores = [10, 5, 7, 1, 9, 6, 8, 3, 4, 2],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
    assert candidate(scores = [10, 20, 30, 20, 10, 40, 50],ages = [1, 2, 3, 1, 2, 3, 4]) == 170
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(scores = [25, 30, 5, 50, 40, 60, 70, 10, 80, 90],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405
    assert candidate(scores = [4, 10, 4, 3, 8, 9],ages = [4, 1, 2, 4, 3, 1]) == 19
    assert candidate(scores = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],ages = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 45
    assert candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40],ages = [1, 3, 2, 5, 4, 7, 6, 8]) == 120
    assert candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
    assert candidate(scores = [40, 20, 30, 10, 50],ages = [2, 1, 3, 4, 5]) == 110
    assert candidate(scores = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45
    assert candidate(scores = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 605
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 55
    assert candidate(scores = [10, 20, 30, 25, 40],ages = [4, 3, 5, 2, 6]) == 95
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 550
    assert candidate(scores = [20, 30, 25, 20, 40, 35, 30, 45, 50, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 245
    assert candidate(scores = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000000000
    assert candidate(scores = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000
    assert candidate(scores = [10, 6, 5, 7, 3, 8],ages = [4, 3, 2, 4, 1, 5]) == 31
    assert candidate(scores = [8, 5, 6, 10, 7, 9, 4, 2, 11, 3],ages = [8, 6, 6, 9, 7, 8, 5, 4, 10, 3]) == 63
    assert candidate(scores = [1000, 500, 250, 750, 100],ages = [20, 25, 30, 35, 40]) == 1250
    assert candidate(scores = [4, 1, 3, 2, 5],ages = [2, 1, 2, 3, 1]) == 8
    assert candidate(scores = [10, 20, 30, 40, 50],ages = [10, 20, 30, 40, 50]) == 150
    assert candidate(scores = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],ages = [1, 2, 1, 3, 2, 4, 3, 5, 4, 5]) == 310
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],ages = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(scores = [10, 9, 2, 5, 3, 7, 1, 8, 6, 4],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
    assert candidate(scores = [1000000, 100000, 10000, 1000, 100, 10, 1],ages = [1, 2, 3, 4, 5, 6, 7]) == 1000000
    assert candidate(scores = [10, 20, 30, 40, 50],ages = [3, 2, 1, 2, 3]) == 120
    assert candidate(scores = [9, 2, 8, 5, 7, 6, 3, 4, 1, 10],ages = [4, 1, 6, 3, 5, 4, 2, 3, 1, 7]) == 46
    assert candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(scores = [100, 200, 300, 400, 500],ages = [5, 4, 3, 2, 1]) == 500
    assert candidate(scores = [100, 200, 300, 200, 100],ages = [1, 2, 3, 4, 5]) == 600
    assert candidate(scores = [9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
    assert candidate(scores = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(scores = [4, 5, 6, 5, 7, 8, 6, 9],ages = [2, 1, 2, 1, 3, 4, 3, 5]) == 46
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 550
    assert candidate(scores = [20, 30, 10, 40, 50],ages = [10, 10, 10, 10, 10]) == 150
    assert candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(scores = [9, 2, 8, 8, 8, 2, 1, 1, 1, 4],ages = [6, 2, 4, 7, 7, 2, 2, 2, 4, 3]) == 34
    assert candidate(scores = [8, 2, 7, 5, 4, 3, 9],ages = [2, 3, 1, 2, 3, 4, 5]) == 24
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(scores = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],ages = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 28
    assert candidate(scores = [15, 20, 5, 10, 25, 30],ages = [5, 5, 2, 3, 5, 5]) == 105
    assert candidate(scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
    assert candidate(scores = [5, 10, 15, 20, 25, 30, 35],ages = [20, 20, 20, 20, 20, 20, 20]) == 140
    assert candidate(scores = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 95
    assert candidate(scores = [8, 6, 7, 5, 3, 0, 9],ages = [1, 2, 2, 3, 3, 3, 4]) == 22
    assert candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 550
    assert candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 20
    assert candidate(scores = [3, 10, 2, 1, 5, 7, 8, 6, 4, 9],ages = [1, 3, 2, 4, 2, 2, 3, 2, 2, 1]) == 43
    assert candidate(scores = [50, 40, 30, 20, 10, 100, 90, 80, 70, 60],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 150
    assert candidate(scores = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 275
    assert candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(scores = [10, 20, 20, 10, 30, 30, 40, 40],ages = [1, 1, 2, 2, 3, 3, 4, 4]) == 190
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
    assert candidate(scores = [10, 20, 20, 10, 30],ages = [1, 2, 3, 4, 5]) == 80
    assert candidate(scores = [1000, 1000, 1000, 1000, 1000],ages = [1, 1, 1, 1, 1]) == 5000
    assert candidate(scores = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55],ages = [3, 1, 2, 4, 5, 1, 2, 3, 4, 5]) == 325
    assert candidate(scores = [50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1]) == 150
    assert candidate(scores = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(scores = [20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5]) == 100
    assert candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(scores = [5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1]) == 15
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
    assert candidate(scores = [100, 200, 150, 100, 50, 250],ages = [5, 4, 3, 2, 1, 6]) == 750
    assert candidate(scores = [3, 1, 2],ages = [1, 1, 1]) == 6
    assert candidate(scores = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(scores = [4, 1, 6, 2, 5, 3],ages = [2, 1, 3, 1, 2, 3]) == 18
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(scores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],ages = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 20
    assert candidate(scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 54
    assert candidate(scores = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],ages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 11
    assert candidate(scores = [15, 30, 10, 20, 50],ages = [5, 10, 15, 20, 25]) == 95
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 350
    assert candidate(scores = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 200
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
    assert candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000000
    assert candidate(scores = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540
    assert candidate(scores = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26
    assert candidate(scores = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 65
    assert candidate(scores = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],ages = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1]) == 75
    assert candidate(scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23
    assert candidate(scores = [1000, 500, 200, 1000, 1000, 500, 200],ages = [2, 1, 3, 2, 3, 1, 3]) == 4000
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 22
    assert candidate(scores = [100, 200, 300, 400, 500, 150, 250, 350, 450, 550],ages = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == 1750
    assert candidate(scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
    assert candidate(scores = [10, 20, 30, 40, 50],ages = [1, 3, 2, 5, 4]) == 90
    assert candidate(scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(scores = [4, 10, 10, 6, 7, 1, 9],ages = [4, 1, 4, 2, 2, 3, 6]) == 23
    assert candidate(scores = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],ages = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 30
    assert candidate(scores = [1, 2, 3, 4, 5],ages = [5, 4, 3, 2, 1]) == 5
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
    assert candidate(scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],ages = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 275
    assert candidate(scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 550
    assert candidate(scores = [5, 4, 3, 2, 1],ages = [1, 2, 3, 4, 5]) == 5
    assert candidate(scores = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(scores = [100, 90, 80, 70, 60],ages = [5, 4, 3, 2, 1]) == 400
    assert candidate(scores = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
    assert candidate(scores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],ages = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1]) == 19
    assert candidate(scores = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],ages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1998046


